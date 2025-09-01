from poke_env.battle import AbstractBattle, Battle, Effect, EmptyMove, Field, Move, MoveCategory, Pokemon, PokemonGender, PokemonType, SideCondition, Status, Target, Weather
from poke_env.player import Player
from poke_env.player.battle_order import BattleOrder, DefaultBattleOrder, DoubleBattleOrder, SingleBattleOrder
from typing import Optional
from poke_env.calc.damage_calc_gen9 import calculate_damage

team = """
Crunchie (Landorus-Therian) @ Rocky Helmet  
Ability: Intimidate  
Shiny: Yes  
Tera Type: Ground  
EVs: 252 Atk / 4 SpD / 252 Spe  
Jolly Nature  
- Stealth Rock  
- Earthquake  
- U-turn  
- Stone Edge  

Ballet (Arceus-Fairy) @ Pixie Plate  
Ability: Multitype  
Shiny: Yes  
Tera Type: Water  
EVs: 240 HP / 252 Def / 16 Spe  
Bold Nature  
- Judgment  
- Thunder Wave  
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
        self.opp_switch_team: bool = False
        self.switch_guesses: list[tuple[float, bool]] = []
        self.lead_mons: list[Pokemon] = [Pokemon(9, species='Landorus-Therian'),Pokemon(9, species='Glimmora'),Pokemon(9, species='Great Tusk'),Pokemon(9, species='')]
        print(self.lead_mons)
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
        
        # Analyse last move
        else:
            print(battle_obj.observations)
            
            
        if battle_obj.active_pokemon != None and battle_obj.opponent_active_pokemon != None and not battle_obj.active_pokemon.fainted:
            
            # Get damage for all moves
            highest_move: Move = list(battle_obj.active_pokemon.moves.values())[0]
            highest_dam: float = -1.0
            for move in battle_obj.available_moves:
                possible_dam: float = self.estimate_damage(battle_obj.active_pokemon, battle_obj.opponent_active_pokemon, move, battle_obj)
                if possible_dam > highest_dam:
                    highest_move = move
                    highest_dam = possible_dam
                    
            if highest_dam != -1.0:
                action = self.create_order(highest_move)
            else:
                # action = switch
                action = self.choose_random_move(battle)
        
        else:
            action = self.choose_random_move(battle)
    
        return action
    
    def get_ideal_switch(self, battle: Battle, opp_switch: bool) -> Optional[Pokemon]:
        '''
        Identifies the ideal pokemon to switch.
        
        Args:
            battle (Battle): The current battle object
            opp_switch (bool): True if evaluating for opponent
        Returns:
            Optional[Pokemon]: Returns the best pokemon to switch into. Returns None if there are no pokemon remaining to switch into.
        '''
        # Initialise switch
        switch: Optional[Pokemon] = None
        
        # Iterate through all Pokemon
        for mon in (battle.opponent if opp_switch else battle.available_switches):
            
            # Check if there are any switches avaialble
            if switch == None:
                switch = mon
            else:
                if self.get_switch_score(battle, switch, False) < self.get_switch_score(battle, mon, False):
                    switch = mon
        
        # Return switch
        return switch
                
    def get_switch_score(self, battle: Battle, switch: Pokemon, opp_switch: bool) -> float:
        '''
        Provides a score of how well a Pokemon would be as a switch into the battle. Considers your pokemon, your team, your opponents pokemon, and your opponents team.
        
        Args:
            battle (Battle): The current battle object
            switch (Pokemon): The pokemon being looked into as a switching option
            opp_switch (bool): True if evaluating your opponent's possible switch
        Returns:
            float: A score for the switch (0 - 1)
        '''
        # Get eval_against
        eval_against: Optional[Pokemon] = battle.active_pokemon if self.will_opponent_switch(battle) > 0.6 and opp_switch else self.guess_opponent_switch(battle)
        
        # Check that switch is valid
        if switch == None or eval_against == None:
            return 0.0
        else:
            # Get mults
            mon_mult: float = self.get_best_mult(eval_against, switch) # How good my pokemon is against their's
            opp_mult: float = self.get_best_mult(switch, eval_against) # How good their pokemon is against mine
            cur_mon_mult: float = self.get_best_mult(eval_against, battle.active_pokemon) # How good my pokemon is against their's
            cur_opp_mult: float = self.get_best_mult(battle.active_pokemon, eval_against) # How good their pokemon is against mine
            
            # Get comparison
            comp: float = (cur_opp_mult/opp_mult) * (mon_mult/cur_mon_mult)
            
            # Calculate score
            if cur_opp_mult > 2 and opp_mult <= 2:
                score: float = 1.0
            elif cur_opp_mult > 1 and opp_mult 
            
            # Return score
            return score
            
            
        
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
                self.switch_guesses.append((swap_odds, False))
                
                # Return swap_odds
                return swap_odds
            else:
                return 0.0   
            
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
        
    def should_switch(self, battle: Battle, ideal_mon: Pokemon) -> bool:
        '''
        Return a boolean indication of whether or not switching is the best choice in the current situation
        
        Args:
            battle (Battle): The current battle object.
            ideal_mon (Pokemon): The pokemon that would be the best to switch to (as defined by ideal_switch)
        Returns:
            bool: Whether we should switch out our current pokemon for ideal_mon
        '''
    
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
        opp_st = self.estimate_stats(opp)
        
        # Consider whether physical or special
        if move.category == MoveCategory.PHYSICAL:
            
            # Get attack & defense stat
            attack = mon.stats['atk'] * (((mon.boosts['atk']+2)/2) if mon.boosts['atk'] > 0 else (2/(2 - mon.boosts['atk'])))
            defense = opp_st['def'] * (((opp.boosts['def']+2)/2) if opp.boosts['def'] > 0 else (2/(2 - opp.boosts['def'])))
            
            # Consider weather
            if Weather.SNOW in battle.weather.keys() or Weather.SNOWSCAPE in battle.weather.keys() and PokemonType.ICE in opp.types:
                defense = defense * 1.5
                
        elif move.category == MoveCategory.SPECIAL:
            
            # Get attack & defense stat
            attack = mon.stats['spa'] * (((mon.boosts['spa']+2)/2) if mon.boosts['spa'] > 0 else (2/(2 - mon.boosts['spa'])))
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
        
        