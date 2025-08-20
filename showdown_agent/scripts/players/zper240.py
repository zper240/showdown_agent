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
        super().__init__(team=team, *args, **kwargs)
        
    def teampreview(self, battle: AbstractBattle):
        return "/team 123456"

    def choose_move(self, battle: AbstractBattle):
        battle_obj: Battle = battle
        # At the start of each battle, set switch_team to False. Will be set to True if the opposing team switches without a pokemon fainting.
        if battle._turn == 3:
            opp_switch_team: bool = False
            opponent_full_team: set[Pokemon] = battle_obj.teampreview_opponent_team
            opponent_mon: Optional[Pokemon] = battle_obj.opponent_active_pokemon
            
            if (opponent_mon != None):
                print()
                print(battle_obj.players)
                print(opponent_mon)
                print(opponent_mon.base_stats)
                print(self.estimate_stats(opponent_mon))
                print(battle_obj.active_pokemon)
                print(battle_obj.active_pokemon.base_stats)
                print(battle_obj.active_pokemon.stats)
                print(self.estimate_stats(battle_obj.active_pokemon))
                # Get list of all my current moves
                available_moves: dict[str, Move] = battle_obj.active_pokemon.moves
                battle_obj.available_moves
                for move in available_moves.values():
                    print(str(move) + ": " + str(self.estimate_damage(battle_obj.active_pokemon, opponent_mon, move, battle)))
            
        return self.choose_random_move(battle)
    
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
                
                
        
        
        