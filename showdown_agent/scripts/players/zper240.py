from poke_env.battle import AbstractBattle, Battle, Effect, EmptyMove, Field, Move, MoveCategory, Pokemon, PokemonGender, PokemonType, SideCondition, Status, Target, Weather
from poke_env.player import Player
from poke_env.player.battle_order import BattleOrder, DefaultBattleOrder, DoubleBattleOrder, SingleBattleOrder
from typing import Optional
from copy import deepcopy

team = """
Crunchie (Landorus-Therian) @ Rocky Helmet  
Ability: Intimidate  
Shiny: Yes  
Tera Type: Ground  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Stealth Rock  
- Earthquake  
- Taunt  
- Stone Edge  

Ballet (Arceus-Fairy) @ Pixie Plate  
Ability: Multitype  
Shiny: Yes  
Tera Type: Water  
EVs: 240 HP / 252 Def / 16 Spe  
Bold Nature  
- Judgment  
- Earth Power  
- Dragon Tail  
- Recover  

Wheels (Koraidon) @ Choice Scarf  
Ability: Orichalcum Pulse  
Tera Type: Fire  
EVs: 252 Atk / 4 SpD / 252 Spe  
Adamant Nature  
- Collision Course  
- Dragon Claw  
- Flare Blitz  
- U-turn  

Flounder (Kyogre) @ Heavy-Duty Boots  
Ability: Drizzle  
Shiny: Yes  
Tera Type: Poison  
EVs: 248 HP / 164 Def / 80 SpA / 16 Spe  
Bold Nature  
IVs: 0 Atk  
- Origin Pulse  
- Thunder  
- Calm Mind  
- Ice Beam  

Sharp (Necrozma-Dusk-Mane) @ Occa Berry  
Ability: Prism Armor  
Shiny: Yes  
Tera Type: Steel  
EVs: 252 Atk / 4 SpD / 252 Spe  
Adamant Nature  
- Dragon Dance  
- Photon Geyser  
- Morning Sun  
- Sunsteel Strike  

Break (Calyrex-Ice) @ Weakness Policy  
Ability: As One (Glastrier)  
Tera Type: Ground  
EVs: 248 HP / 252 Atk / 8 SpD  
Brave Nature  
IVs: 0 Spe  
- Trick Room  
- Swords Dance  
- Glacial Lance  
- High Horsepower  
"""

class CustomAgent(Player):
    
    def __init__(self, *args, **kwargs):
        ## Important Info
        self.opp_switch_team: bool = False
        self.switch_guesses: list[tuple[float, bool]] = []
        self.turns = []
        self.last_turn = 0
        self.record_guess = True
        self.last_move: Optional[SingleBattleOrder] = None
        self.lead_mons: list[Pokemon] = [Pokemon(9, species='Landorus-Therian'),Pokemon(9, species='Glimmora'),Pokemon(9, species='Great Tusk'),Pokemon(9, species='Deoxys-Speed'),Pokemon(9, species='Eternatus')]
        print(self.lead_mons)
        
        ## Testing Booleans
        self.full_random = False
        self.spec_strat = True
        self.stat_moves = True
        self.smart_switch = True
        
        ## Initialise
        super().__init__(team=team, *args, **kwargs)
        
    def teampreview(self, battle: AbstractBattle):
        return "/team 123456"
                
    def choose_move(self, battle: AbstractBattle):
        
        # Make battle_obj
        battle_obj: Battle = battle
        
        # Define action variable
        action: Optional[SingleBattleOrder]
        
        # At the start of each battle, set switch_team to False. Will be set to True if the opposing team switches without a pokemon fainting.
        if battle._turn == 1:
            self.opp_switch_team = False
            self.switch_guesses = []
            self.turns = [self.TurnState(battle_obj)]
            print()
            print()
            
        # Check if switch team and record turn
        elif self.last_turn != battle_obj.turn:
            self.record_guess = True
            self.switch_guesses[-1] = (self.switch_guesses[0],self.turns[-1].opp_switched(self.turns[-2],self.last_move != self.create_order(Move('dragontail',9))))
            self.turns.append(self.TurnState(battle_obj))
            if not self.opp_switch_team:
                self.opp_switch_team = self.turns[-1].opp_switched(self.turns[-2],self.last_move != self.create_order(Move('dragontail',9)))
            if self.turns[-1].mon_fainted(self.turns[-2]):
                # print("Mon fainted!")
                pass
            
        if battle_obj.active_pokemon != None and battle_obj.opponent_active_pokemon != None and not self.full_random:
            
            # Get best move:
            dam_move: Move = self.get_best_move(battle)
            
            # Get best switch
            switch = self.get_ideal_switch(battle)
            
            should_switch: bool = self.should_switch(battle, switch) and self.smart_switch
            
            # Make move
            if dam_move != None:
                action = self.create_order(dam_move)
            else:
                # action = switch
                action = self.choose_random_move(battle)
        
        else:
            action = self.choose_random_move(battle)

        self.last_move = action
        
        print(action)
        return action
    
    def get_most_damage(self, battle: Battle, for_opp: bool = False, switch_mon: Optional[Pokemon] = None) -> float:
        '''
        Gets the most damage able to be done
        
        Args:
            battle (Battle): The current battle object
            for_opp (bool): True if analysing for opponent - default False
            switch_mon (Pokemon): Mon analysed to switch into - default None (means analyse pokemon currently in battle)
        Returns:
            float: The damage done
        '''
        # Get pokemon to evaluate
        eval_for: Pokemon = (switch_mon if switch_mon != None else battle.active_pokemon) if not for_opp else battle.opponent_active_pokemon
        eval_against: Pokemon = battle.opponent_active_pokemon if not for_opp else (switch_mon if switch_mon != None else battle.active_pokemon)
        
        # Get highest damage
        if len(eval_for.moves) < 1:
            return -1.0
        move_list: list[Move] = list(eval_for.moves.values())
        highest_dam: float = -1.0
        
        for move in move_list:
            possible_dam: float = self.estimate_damage(eval_for, eval_against, move, battle)
            if possible_dam > highest_dam:
                highest_dam = possible_dam
                
        # Return highest damage
        return highest_dam
    
    def get_best_move(self, battle: Battle, for_opp: bool = False, switch_mon: Optional[Pokemon] = None) -> Optional[Move]:
        '''
        Gets the highest damaging move
        
        Args:
            battle (Battle): The current battle object
            for_opp (bool): True if analysing for opponent - default False
            switch_mon (Pokemon): Mon analysed to switch into - default None (means analyse pokemon currently in battle)
        Returns:
            Optional[Move]: The highest damaging move.
        '''
        # Define healing moves
        healing_moves: list[str] = ['healorder','lunarblessing','milkdrink','moonlight','morningsun','purify','recover','rest','roost','shoreup','slackoff','softboiled','strengthsap','synthesis']

        # Get pokemon to evaluate
        eval_for: Pokemon = (switch_mon if switch_mon != None else battle.active_pokemon) if not for_opp else battle.opponent_active_pokemon
        eval_against: Pokemon = battle.opponent_active_pokemon if not for_opp else (switch_mon if switch_mon != None else battle.active_pokemon)
        
        # Get damage for all moves
        if len(eval_for.moves) < 1:
            return None
        move_list: list[Move] = list(eval_for.moves.values())
        highest_move: Move = move_list[0]
        highest_dam: float = -1.0
        
        for move in move_list:
            possible_dam: float = self.estimate_damage(eval_for, eval_against, move, battle)
            if possible_dam > highest_dam:
                highest_move = move
                highest_dam = possible_dam

        # Consider status moves
        if not for_opp and switch_mon == None:
            heal_move: Optional[Move] = None
            stat_move: Optional[Move] = None
            for mov in battle.available_moves:
                if mov.category == MoveCategory.STATUS and mov.id != 'trickroom':
                    if mov.id in healing_moves and heal_move == None:
                        heal_move = mov
                    elif stat_move == None:
                        stat_move = mov
                if heal_move != None and stat_move != None:
                    break
            # Do heal or status moves
            if heal_move != None and battle.active_pokemon.current_hp_fraction < 0.55 and self.get_most_damage(battle) < battle.active_pokemon.max_hp * 0.5:
                return heal_move
            if stat_move != None and battle.active_pokemon.current_hp_fraction > 0.7 and self.is_resistant(battle) and not self.will_die_switch(battle, battle.active_pokemon):
                return stat_move
        
        # Return highest damage move
        if highest_dam != -1.0:
            return highest_move
        else:
            return None
        
    def is_resistant(self, battle: Battle) -> bool:
        '''
        Checks if def_mon is resistant to atk_mon (to best of knowledge)
        '''
        typ_res: bool = self.get_best_mult(battle.active_pokemon, battle.opponent_active_pokemon) <= 1
        
        dam_res: bool = self.get_most_damage(battle) * 2 < battle.active_pokemon.current_hp
        
        return typ_res and dam_res
    
    def will_die_switch(self, battle: Battle, switch_mon: Pokemon) -> bool:
        '''
        Checks if mon will die upon switching in (or after doing status move)
        
        Args:
            battle (Battle): The current battle object
            switch_mon (Pokemon): Mon looking at being switched in
        Returns:
            bool: True if pokemon will die upon switching in
        '''
        # Check if moves are known
        if len(battle.opponent_active_pokemon.moves) == 0:
            return switch_mon.current_hp > 0.35 if self.is_faster(battle, switch_mon, battle.opponent_active_pokemon) else switch_mon.current_hp > 0.5
        
        # Get max damage of opponent move on switch mon
        dam: float = self.get_most_damage(battle, True, switch_mon)
        
        # Get multiplier
        mult: float = 1 if self.is_faster(battle, switch_mon, battle.opponent_active_pokemon) else (2 if switch_mon.species == battle.active_pokemon.species else 1.5)
        
        # Check if does too much damage
        return dam * mult >= switch_mon.current_hp
    
    def will_ko(self, battle: Battle, mon: Pokemon) -> bool:
        '''
        Checks if it will knockout in one move.
        
        Args:
            battle (Battle): The current battle object
            mon (Pokemon): Pokemon being looked into
        Returns:
            bool: True if will OHKO
        '''
        return self.get_most_damage(battle, False, mon) > self.estimate_stats(battle.opponent_active_pokemon)['hp'] * battle.opponent_active_pokemon.current_hp_fraction
    
    def should_switch(self, battle: Battle, mon: Optional[Pokemon]) -> bool:
        '''
        Calculates if you should switch or not
        
        Args:
            battle (Battle): The current battle object
            mon (Pokemon): Pokemon to switch into
        Returns:
            bool: True if you should switch
        '''
        # Compare this switch to current pokemon
        if mon.species == battle.active_pokemon.species or mon == None:
            return False
        
        # Check if Pokemon will die from hazards or will kill opponents pokemon on
        hazard_penalty: float = 0
        if battle.side_conditions.get("stealthrock"):
            rock_mult: float = max(battle.active_pokemon.damage_multiplier(PokemonType.ROCK), 1)
            hazard_penalty += 0.125 * rock_mult
        if battle.side_conditions.get("spikes"):
            layers = battle.side_conditions["spikes"]
            match layers:
                case 1:
                    hazard_penalty += 1/8
                case 2:
                    hazard_penalty += 1/6
                case 3:
                    hazard_penalty += 1/4
                case _:
                    pass
        if hazard_penalty >= battle.active_pokemon.current_hp_fraction:
            return False
        if self.will_die_switch(battle, mon):
            return False
        if self.will_ko(battle, mon) and self.is_faster(battle, mon, battle.opponent_active_pokemon) and battle.active_pokemon.fainted:
            return True
        
        # Get switch score
        eval_against: Optional[Pokemon] = battle.active_pokemon if self.will_opponent_switch(battle) > 0.6 else self.guess_opponent_switch(battle)
        cur_sc: float = self.get_switch_score(battle, battle.active_pokemon)
        swi_sc: float = self.get_switch_score(battle, mon)
        
        # If switch score is much higher than current score, switch
        if cur_sc > swi_sc + 1 or cur_sc > 2 * swi_sc:
            return True
        # If current score is much higher than switch score, don't switch
        if swi_sc > cur_sc + 1 or swi_sc > 2 * cur_sc:
            return False
        
        # Get opp_mult ratio and mon_mult ratio
        mon_mult: float = self.get_best_mult(eval_against, mon) # How good my pokemon is against their's
        opp_mult: float = self.get_best_mult(mon, eval_against) # How good their pokemon is against mine
        cur_mon_mult: float = self.get_best_mult(eval_against, battle.active_pokemon) # How good my pokemon is against their's
        cur_opp_mult: float = self.get_best_mult(battle.active_pokemon, eval_against) # How good their pokemon is against mine
        mon_mult_rat: float = (mon_mult/cur_mon_mult) # How much better the switch is for me (atk)
        opp_mult_rat: float = (opp_mult/cur_opp_mult) # How much better the switch is for them (atk)
        
        # Evaluate
        if opp_mult_rat > 1 and mon_mult_rat < 8:
            return False
        elif cur_mon_mult >= 2 and cur_opp_mult < 1:
            return False
        elif opp_mult_rat == 1 and mon_mult_rat >= 4:
            return True
        elif opp_mult_rat == 1 and opp_mult <= 1 and mon_mult_rat >= 2 and mon_mult >= 2 and self.estimate_stats(eval_against)['spe'] < mon.stats['spe']:
            return True
        elif opp_mult_rat <= 0.5 and opp_mult < 0.5 and mon_mult >= 1:
            return True
        elif opp_mult_rat < 0.5:
            return True
        elif cur_mon_mult < 0.5 and mon_mult_rat > 1:
            return True
        else:
            return False

    def is_faster(self, battle: Battle, mon_1: Pokemon, mon_2: Pokemon) -> bool:
        '''
        Returns true if mon_1 is faster than mon_2

        Args:
            battle (Battle): The current battle object
            mon_1 (Pokemon): The first pokemon
            mon_2 (Pokemon): The second pokemon
        Returns:
            bool: True if mon_1 is faster than mon_2
        '''
        # Get speeds
        spe_1: float = self.get_stats(mon_1) * (((mon_1.boosts['spe']+2)/2) if mon_1.boosts['spe'] > 0 else (2/(2 - mon_1.boosts['spe'])))
        spe_2: float = self.get_stats(mon_2) * (((mon_2.boosts['spe']+2)/2) if mon_2.boosts['spe'] > 0 else (2/(2 - mon_2.boosts['spe'])))
        
        # Consider choicescarf
        if mon_1.item == 'choicescarf':
            spe_1 *= 1.5
        if mon_2.item == 'choicescarf':
            spe_2 *= 1.5
        
        # Compare speeds
        if Field.TRICK_ROOM in battle.fields.keys():
            return spe_2 > spe_1
        else:
            return spe_1 > spe_2
        
    def get_ideal_switch(self, battle: Battle) -> Optional[Pokemon]:
        '''
        Identifies the ideal pokemon to switch.
        
        Args:
            battle (Battle): The current battle object
        Returns:
            Optional[Pokemon]: Returns the best pokemon to switch into. Returns None if there are no pokemon remaining to switch into.
        '''
        # Initialise switch
        switch: Optional[Pokemon] = None
        
        # Iterate through all Pokemon
        for mon in battle.available_switches:
            
            # Check if there are any switches avaialble
            if switch == None:
                switch = mon
            else:
                if self.get_switch_score(battle, switch) < self.get_switch_score(battle, mon):
                    switch = mon
        
        # Return switch
        return switch
                
    def get_switch_score(self, battle: Battle, switch: Pokemon) -> float:
        '''
        Provides a score of how well a Pokemon would be as a switch into the battle. Considers your pokemon, your team, your opponents pokemon, and your opponents team.
        
        Args:
            battle (Battle): The current battle object
            switch (Pokemon): The pokemon being looked into as a switching option
        Returns:
            float: A score for the switch
        '''
        # Get eval_against
        eval_against: Optional[Pokemon] = battle.opponent_active_pokemon if self.will_opponent_switch(battle) > 0.6 else self.guess_opponent_switch(battle)
        
        # Check that switch is valid
        if switch == None or eval_against == None:
            return 0.0
        elif self.will_die_switch(battle, switch) and switch.species != battle.active_pokemon.species:
            return 0.0
        else:
            # Get mults
            mon_mult: float = self.get_best_mult(eval_against, switch) # How good my pokemon is against their's
            opp_mult: float = self.get_best_mult(switch, eval_against) # How good their pokemon is against mine
            cur_mon_mult: float = self.get_best_mult(eval_against, battle.active_pokemon) # How good my pokemon is against their's
            cur_opp_mult: float = self.get_best_mult(battle.active_pokemon, eval_against) # How good their pokemon is against mine
            
            # Get comparison
            comp: float = (cur_opp_mult/opp_mult) * (mon_mult/cur_mon_mult)

            # Consider boosts on active pokemon
            if switch.species == battle.active_pokemon.species:
                comp *= (1 + float(sum(battle.active_pokemon.boosts.values()))/2)
            
            # Return comp
            return comp

    def will_opponent_switch(self, battle: Battle) -> float:
        '''
        Attempts to guess if the opponent is going to switch
        
        Args:
            battle (Battle): The current battle object
        Returns:
            float: The calculated likelihood of a switch (non-statistical analysis, 0-1)
        '''
        # Check that opponent is a switch team
        if not self.opp_switch_team:
            return 0.0
        else:
            # Guess opponent switch
            switch_mon: Optional[Pokemon] = self.guess_opponent_switch(battle)
            
            # Check if it is a viable switch
            if not switch_mon == None or not switch_mon.species == battle.opponent_active_pokemon.species:
            
                # Get mults
                mon_mult: float = self.get_best_mult(switch_mon, battle.active_pokemon) # How good my pokemon is against their's
                opp_mult: float = self.get_best_mult(battle.active_pokemon, switch_mon) # How good their pokemon is against mine
                cur_mon_mult: float = self.get_best_mult(battle.opponent_active_pokemon, battle.active_pokemon) # How good my pokemon is against their's
                cur_opp_mult: float = self.get_best_mult(battle.active_pokemon, battle.opponent_active_pokemon) # How good their pokemon is against mine
                
                # Get comparison
                comp: float = (opp_mult/cur_opp_mult) * (cur_mon_mult/mon_mult)
                
                # Estimate likelihood
                swap_odds: float = 1.0 if comp > 4 else (0.0 if comp < 1 else ((comp - 1) / 3))
                
                # Add likelihood to list
                if self.record_guess:
                    self.switch_guesses.append((swap_odds, False))
                    self.record_guess = False
                
                # Adjust accuracy for past guesses - Do not do anymore
                swap_odds = 0
                
                # Return swap_odds
                return swap_odds
            else:
                return 0.0   
    
    class TurnState():
        
        def __init__(self, battle: Battle):
            self._battle_state: Battle = deepcopy(battle)
            self._mon: Pokemon = deepcopy(battle.active_pokemon)
            self._opp: Pokemon = deepcopy(battle.opponent_active_pokemon)
            
        def get_state(self):
            '''
            Returns current state of the battle
            
            Args:
                None
            Returns:
                Battle: The battle object (preserved)
            '''
            return self._battle_state
        
        def mon_fainted(self, other) -> bool:
            '''
            Checks if our current pokemon fainted
            
            Args:
                other: The next TurnState object (being compared to)
            Returns:
                bool: True if our mon fainted
            '''
            # Find pokemon
            for mon in other._battle_state.team.values():
                if self._mon.species == mon.species:
                    if self._mon.fainted or mon.fainted:
                        return True
                    else:
                        return False
            return False
        
        def opp_fainted(self, other) -> bool:
            '''
            Checks if their current pokemon fainted
            
            Args:
                other: The next TurnState object (being compared to)
            Returns:
                bool: True if their mon fainted
            '''
            # Find pokemon
            for mon in other._battle_state.opponent_team.values():
                if self._opp.species == mon.species:
                    if self._opp.fainted or mon.fainted:
                        return True
                    else:
                        return False
            return False
        
        def opp_switched(self, other, last_move_d_tail) -> bool:
            '''
            Checks if they switched
            
            Args:
                other: The next TurnState object (being compared to)
            Returns:
                bool: True if they switched
            '''
            # Find pokemon
            if self._opp.species != other._opp.species and not self.opp_fainted(other) and not last_move_d_tail:
                return True
            else:
                return False
            
    def get_opp_team_total(self, battle: Battle) -> list[Pokemon]:
        '''
        Returns all known details about the opponents team
        
        Args:
            battle (Battle): The current battle object
        Returns:
            list[Pokemon]: The list of Pokemon objects
        '''
        # Make complete team list for opponent's team
        opp_team: list[Pokemon] = []
        found: bool = False
        for pre_mon in battle.teampreview_opponent_team:
            found = False
            for mon in battle.opponent_team.values():
                if mon.species == pre_mon.species:
                    found = True
                    opp_team.append(mon)
                    break
            if not found:
                opp_team.append(pre_mon)
        
        # Return team
        return opp_team
    
    def get_opp_available_switches(self, battle: Battle) -> list[Pokemon]:
        '''
        Returns all possible switches for your opponent
        
        Args:
            battle (Battle): The current battle object
        Returns:
            list[Pokemon]: All non-active, non-fainted pokemon in your opponents team
        '''
        # Get opp team and initialise switches
        opp_team: list[Pokemon] = self.get_opp_team_total(battle)
        switches: list[Pokemon] = []
        
        # Go through opponents team
        for mon in opp_team:
            if not mon.fainted and mon.species != battle.opponent_active_pokemon.species:
                switches.append(mon)
        
        # Return switches
        return switches
                
    def is_better_switch(self, mon_mult_1: float, opp_mult_1: float, mon_mult_2: float, opp_mult_2: float, for_opp: bool) -> bool:
        '''
        Determines whether the current option is a better switch
        
        Args:
            mon_mult_1 (float): Multiplier of how good my pokemon is against their's for first option
            opp_mult_1 (float): Multiplier of how good their pokemon is against mine for first option
            mon_mult_2 (float): Multiplier of how good my pokemon is against their's for second option
            opp_mult_2 (float): Multiplier of how good their pokemon is against mine for second option
            for_opp (bool): True if it is better for opponent, False if better for self
        Returns:
            bool: True if second option is better than first
        '''
        # Get complete value
        a: bool = mon_mult_1 >= mon_mult_2
        b: bool = opp_mult_1 >= opp_mult_2
        c: bool = for_opp
        d: bool = (mon_mult_2/opp_mult_2) > 1
        
        # Case
        value: int = 8 * a + 4 * b + 2 * c + d
        match value:
            case 1 | 2 | 4 | 5 | 10 | 11 | 13 | 14:
                return True
            case _:
                return False
        
    def guess_opponent_switch(self, battle: Battle) -> Optional[Pokemon]:
        '''
        Attempts to guess which pokemon the opponent will switch into - may return the current pokemon (i.e. no switch)
        
        Args:
            battle (Battle): The current battle object
        Returns:
            Pokemon: The pokemon the opponent will probably switch into
        '''
        # Get opponents team
        opp_team: list[Pokemon] = self.get_opp_available_switches(battle)
        
        # Check that an opponent switch is possible
        if len(opp_team) == 0:
            return battle.active_pokemon
        
        # Initilaise best mult
        best_mon_mult: float = -1.0
        best_opp_mult: float = 5.0
        best_mon: Optional[Pokemon] = None
    
        # Go through opp_team
        for mon in opp_team:
            # Get mon_mult and opp_mult
            mon_mult: float = self.get_best_mult(mon, battle.active_pokemon) # How good my pokemon is against their's
            opp_mult: float = self.get_best_mult(battle.active_pokemon, mon) # How good their pokemon is against mine
            
            # Assess if better than current best (for opp)
            if self.is_better_switch(best_mon_mult, best_opp_mult, mon_mult, opp_mult, True):
                best_mon = mon
                best_mon_mult = mon_mult
                best_opp_mult = opp_mult
        
        # Return the best switch
        return best_mon
    
    def get_best_mult(self, def_mon: Pokemon, atk_mon: Pokemon) -> float:
        '''
        Returns the best multiplier for the atk_mon against the def_mon based on types and (known) moves in atk_mon
        
        Args:
            def_mon (Pokemon): The pokemon being attacked
            atk_mon (Pokemon): The pokemon attacking
        Returns:
            float: The highest multiplier of the atk_mon against the def_mon
        '''
        # Initialise atk_types
        atk_types: set = {}
        
        # Add types of atk_mon to atk_types
        for typ in atk_mon.types:
            atk_types.add(typ)
        
        # Add types from (known) moves in atk_mon
        for mov in atk_mon.moves.values():
            atk_types.add(mov.type)
            
        # Get best multiplier
        best_mult: float = -1
        for typ in atk_types:
            mult: float = def_mon.damage_multiplier(typ)
            if mult > best_mult:
                best_mult = mult
        
        # Return mult
        return mult if mult != 0 else 0.001
    
    def estimate_damage(self, mon: Pokemon, opponent: Pokemon, move: Move, battle: Battle) -> float:
        '''
        Estimates the damage done on a pokemon by a move.
        
        Args:
            mon (Pokemon): Your own pokemon.
            opponent (Pokemon): Your opponents pokemon.
            move (Move): The move you are wanting to use.
            battle (Battle): The current battle.
        Returns:
            float: The expected damage to be dealt
        '''
        # Base power
        base_power: float = move.base_power
        
        # Own Pokemon Level
        self_level: int = mon.level
        
        # Attack/Defence Ratio - consider SNOW & SNOWSCAPE 
        a_d_ratio: float = self.attack_defense_ratio(mon, opponent, move, battle)
        # Get damage before modification
        unmodified_damage: float = ((((2 * self_level)/5)+2)/50 * a_d_ratio * base_power + 2) if move.category != MoveCategory.STATUS else 0
        
        # Initialise damage
        damage: float = unmodified_damage
        
        # Consider if opponent is not grounded and ground moves
        if not battle.is_grounded(opponent) and move.type == PokemonType.GROUND and not Field.GRAVITY in list(battle.fields.keys()):
            damage = 0
            
        # Consider if your pokemon is burned
        if mon.status == Status.BRN:
            damage = damage * 0.5
        
        # Get effectiveness (based on types)
        effectiveness: float = opponent.damage_multiplier(move)
        
        # Get effcts of weather
        weather: float = self.weather_multiplier(list(battle.weather.keys()), move)
        
        # Get effects of abilities
        abilities: float = self.abiltiies_multiplier(mon, opponent, move, battle)
        
        # Get effects of fields
        fields: float = self.field_multiplier(mon, opponent, move, battle)
        
        # Get effects of STAB
        stab: float = self.stab_multiplier(mon, move)
        
        # Calculate damage
        damage = damage * effectiveness * weather * abilities * fields * stab
        
        # Return damage
        return damage
    
    def attack_defense_ratio(self, mon: Pokemon, opp: Pokemon, move: Move, battle: Battle) -> float:
        '''
        Calculates the attach/defense ratio for damage calculations
        
        Args:
            mon (Pokemon): Your pokemon.
            opp (Pokemon): Opponent pokemon.
            move (Move): The desired move.
            battle (Battle): The current battle object.
        Returns:
            float: The ratio.
        '''
        # Initialise attack/defense
        attack: float
        defense: float
        
        # Get opponent pokemons estimated stats
        mon_st = self.get_stats(mon)
        opp_st = self.get_stats(opp)
        
        # Consider whether physical or special
        if move.category == MoveCategory.PHYSICAL:
            
            # Get attack & defense stat
            attack = mon_st['atk'] * (((mon.boosts['atk']+2)/2) if mon.boosts['atk'] > 0 else (2/(2 - mon.boosts['atk'])))
            defense = opp_st['def'] * (((opp.boosts['def']+2)/2) if opp.boosts['def'] > 0 else (2/(2 - opp.boosts['def'])))
            
            # Consider weather
            if Weather.SNOW in battle.weather.keys() or Weather.SNOWSCAPE in battle.weather.keys() and PokemonType.ICE in opp.types:
                defense = defense * 1.5
                
        elif move.category == MoveCategory.SPECIAL:
            
            # Get attack & defense stat
            attack = mon_st['spa'] * (((mon.boosts['spa']+2)/2) if mon.boosts['spa'] > 0 else (2/(2 - mon.boosts['spa'])))
            defense = opp_st['spd'] * (((opp.boosts['spd']+2)/2) if opp.boosts['spd'] > 0 else (2/(2 - opp.boosts['spd'])))
            
            # Consider weather
            if Weather.SANDSTORM in battle.weather.keys() and PokemonType.ROCK in opp.types:
                defense = 1.5 * defense
        
        else:
            # Status Move
            attack = 0
            defense = 1
            
        # Return a2d ratio
        return attack/defense
    
    def weather_multiplier(self, weathers: list[Weather], move: Move) -> float:
        '''
        Calculates the multiplier for a move based on the available weathers
        
        Args:
            weathers (list[Weather]): List of weathers in battle. May be empty.
            move (Move): The move to be used in battle.
        Returns:
            float: The multiplier.
        '''
        # Initialise multiplier
        mult: float = 1.0
        
        # Consider weathers
        for weather in weathers:
            if weather == Weather.SUNNYDAY:
                if move.type == PokemonType.FIRE:
                    mult = mult * 1.5
                elif move.type == PokemonType.WATER:
                    mult = mult * 0.5
            elif weather == Weather.RAINDANCE:
                if move.type == PokemonType.FIRE:
                    mult = mult * 0.5
                elif move.type == PokemonType.WATER:
                    mult = mult * 1.5
                    
        # Return multiplier
        return mult
    
    def abiltiies_multiplier(self, mon: Pokemon, opp: Pokemon, move: Move, battle: Battle) -> float:
        '''
        Calculates the multiplier for a move due to the abilities
        
        Args:
            mon (Pokemon): Your pokemon.
            opp (Pokemon): Opponent pokemon.
            move (Move): The move being considered.
            battle (Battle): Battle object.
        Returns:
            float: The multiplier
        '''
        # Initialise multiplier
        mult: float = 1.0
        
        # Get abilties
        abil = mon.ability
        obil = opp.ability
        
        # Check for opponent abilities
        if obil != None:
            match obil.lower():
                case "dry skin":
                    if move.type == PokemonType.FIRE:
                        mult = mult * 1.25
                    elif move.type == PokemonType.WATER:
                        mult = 0
                case "earth eater":
                    if move.type == PokemonType.GROUND:
                        mult = 0
                case "filter" | "prism armor" | "solid rock":
                    if opp.damage_multiplier(move) >= 2:
                        mult = mult * 0.75
                case "flash fire":
                    mult = 0
                case "fluffy":
                    if move.category == MoveCategory.PHYSICAL:
                        mult = 0.5 * mult
                    if move.type == PokemonType.FIRE:
                        mult = 2 * mult
                case "heatproof":
                    if move.type == PokemonType.FIRE:
                        mult = mult * 0.5
                case "ice face":
                    if move.category == MoveCategory.PHYSICAL:
                        mult = 0
                case "levitate":
                    if move.type == PokemonType.GROUND and not Field.GRAVITY in list(battle.fields.keys()):
                        mult = 0
                case "motor drive":
                    if move.type == PokemonType.ELECTRIC:
                        mult = 0
                case "multiscale" | "shadow shield":
                    if opp.current_hp_fraction == 1:
                        mult = mult * 0.5
                case "purifying salt":
                    if move.type == PokemonType.GHOST:
                        mult = mult * 0.5
                case "sap sipper":
                    if move.type == PokemonType.GRASS:
                        mult = 0
                case "thick fat":
                    if move.type == PokemonType.ICE or move.type == PokemonType.FIRE:
                        mult = mult * 0.5
                case "volt absorb":
                    if move.type == PokemonType.ELECTRIC:
                        mult = 0
                case "water absorb":
                    if move.type == PokemonType.WATER:
                        mult = 0
                case "water bubble":
                    if move.type == PokemonType.FIRE:
                        mult = mult * 0.5
                case "well-baked body":
                    if move.type == PokemonType.FIRE:
                        mult = 0
                case "wonder guard":
                    if opp.damage_multiplier(move) < 2:
                        mult = 0
                case _:
                    mult = mult
        
        # Return the multiplier
        return mult
    
    def field_multiplier(self, mon: Pokemon, opp: Pokemon, move: Move, battle: Battle) -> float:
        '''
        Calculates the multiplier due to the field.
        
        Args:
            mon (Pokemon): Your own pokemon
            opp (Pokemon): Opponents pokemon
            move (Move): The move you want to use
            battle (Battle): The current battle
        Returns:
            float: The multiplier
        '''
        # Initialise multiplier
        mult: float = 1.0
        
        # Go through all fields in the battle
        for field in battle.fields.keys():
            
            # Case statement to adjust multiplier
            match field:
                case Field.ELECTRIC_TERRAIN:
                    if move.type == PokemonType.ELECTRIC:
                        mult = mult * 1.5
                case Field.GRASSY_TERRAIN:
                    if move.type == PokemonType.GRASS:
                        mult = mult * 1.5
                case Field.MUD_SPORT:
                    if move.type == PokemonType.ELECTRIC:
                        mult = mult * 0.5
                case Field.PSYCHIC_TERRAIN:
                    if move.type == PokemonType.PSYCHIC:
                        mult = mult * 1.5
                case Field.WATER_SPORT:
                    if move.type == PokemonType.FIRE:
                        mult = mult * 0.5
                case _:
                    mult = mult
        
        # Return multiplier
        return mult
    
    def stab_multiplier(self, mon: Pokemon, move: Move) -> float:
        '''
        Calculates the multiplier caused by STAB (Same Type Attack Boost)
        
        Args:
            mon (Pokemon): Your pokemon.
            move (Move): Desired move.
        Returns:
            float: The calculated multiplier
        '''
        # Initialise multiplier
        mult: float = 1.0
        
        # Check if STAB
        if mon._terastallized and mon.tera_type == move.type and mon.tera_type in mon.original_types:
            mult = mult * 2
        elif mon._terastallized and mon.tera_type == move.type:
            mult = mult * 1.5
        elif not mon._terastallized and move.type in mon.original_types:
            mult = mult * 1.5
        else:
            mult = mult * 1.0

        # Return mult
        return mult
    
    def estimate_stats(self, opp: Pokemon) -> dict[str, int]:
        '''
        Estimates the stats of an opponents pokemon. Note that IV's are always assumed to be 31.
        
        Args:
            mon (Pokemon): The opponenets pokemon to estimate stats for.
        Returns:
            dict[str, int]: Dictionary containing the estimated statistics.
        '''
        # Get pokemon classification
        is_attack_mon: bool = self.is_attack_mon(opp)
        
        # Get base stats 
        opp_bs: dict[str, int] = opp.base_stats
        
        # Define EV constants
        EV_MAX: int = 252
        EV_MIN: int = 0
        
        # Define stat, ev, & level variable
        stat: int
        ev: int
        lvl: int = opp.level
        
        # Define est_stats
        est_stats: dict[str, int] = {}
        
        # Figure out if hp_boost mon
        hp_boost: bool = abs(opp_bs['def'] - opp_bs['spd']) > 25 and opp_bs['hp'] < 125
        
        # Go through stats
        for st in opp_bs.keys():
            
            # Estimate whether EV has been boosted on the stat
            match st:
                case 'hp' if (hp_boost and not is_attack_mon):
                    ev = EV_MAX
                case 'def' if (hp_boost and opp_bs['def'] <= opp_bs['spd'] or not hp_boost and not is_attack_mon):
                    ev = EV_MAX
                case 'spd' if (hp_boost and opp_bs['def'] > opp_bs['spd'] or not hp_boost and not is_attack_mon):
                    ev = EV_MAX
                case 'atk' if (is_attack_mon and opp_bs['atk'] >= opp_bs['spa']):
                    ev = EV_MAX
                case 'spa' if (is_attack_mon and opp_bs['atk'] < opp_bs['spa']):
                    ev = EV_MAX
                case 'spe' if (is_attack_mon):
                    ev = EV_MAX
                case _:
                    ev = EV_MIN
            
            # Calculate the stat
            base_calc: int = (2 * opp_bs[st] + 31 + ev/4) * lvl/100
            if st == 'hp':
                # HP specific calculation
                stat = int(base_calc + lvl + 10)
            else:
                # Figure out if is boosted by nature
                nature_boost: bool = (is_attack_mon and ev and (bool(opp_bs['spe'] > 130) ^ bool(st == 'spe'))) or (not is_attack_mon and (bool(opp_bs['def'] < opp_bs['spd']) ^ bool(st == 'spd')))
                stat = int(float(base_calc + 5) * (1.1 if nature_boost else 1.0))

            # Add stat to dictionary
            est_stats.update({st: stat})
            
        # Return estimated stats
        return est_stats
    
    def is_attack_mon(self, mon: Pokemon) -> bool:
        '''
        Classifies if a pokemon is an attacking mon or a defensive mon
        
        Args:
            mon (Pokemon): The pokemon to be classified.
        Returns:
            bool: True if the pokemon is classified as an attacker. False if the pokemon is a defensive mon.
        '''
        # Check if atk or spa is high
        if mon.base_stats['atk'] > 130 or mon.base_stats['spa'] > 130 or mon.base_stats['spe'] > 130:
            return True
        else:
            return False
        
    def is_special_mon(self, mon: Pokemon) -> bool:
        '''
        Classifies a pokemon as specially of physically strong
        
        Args:
            mon (Pokemon): The pokemon being investigated
        Returns:
            bool: True if it is a special pokemon.
        '''
        # Find if this is an attack mon
        is_attack: bool = self.is_attack_mon(mon)
        
        # Find if it is special
        if is_attack:
            is_special: bool = mon.base_stats['spa'] > mon.base_stats['atk']
        else:
            is_special: bool = mon.base_stats['spd'] > mon.base_stats['def']
        
        # Return is_special
        return is_special
        
    def get_stats(self, mon: Pokemon) -> dict[str, int]:
        '''
        Returns the stats of the mon, known if possible, estimated if not
        
        Args:
            mon (Pokemon): The pokemon to get stats of
        Returns:
            dict[str, int]: List of stats
        '''      
        if list(mon.stats.values())[0] != None:
            return mon.stats
        else:
            return self.estimate_stats(mon)