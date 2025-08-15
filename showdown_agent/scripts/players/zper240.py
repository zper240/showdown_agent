from poke_env.battle import AbstractBattle, Battle, Effect, EmptyMove, Field, Move, MoveCategory, Pokemon, PokemonGender, PokemonType, SideCondition, Status, Target, Weather
from poke_env.player import Player
from poke_env.player.battle_order import BattleOrder, DefaultBattleOrder, DoubleBattleOrder, SingleBattleOrder
from typing import Optional

team = """
Crunchie (Landorus-Therian) @ Focus Sash  
Ability: Intimidate  
Shiny: Yes  
Tera Type: Ground  
EVs: 248 HP / 8 Atk / 252 Def  
Impish Nature  
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
        super().__init__(team=team, *args, **kwargs)

    def choose_move(self, battle: AbstractBattle):
        battle_obj: Battle = battle
        # At the start of each battle, set switch_team to False. Will be set to True if the opposing team switches without a pokemon fainting.
        if battle._turn == 1:
            opp_switch_team: bool = False
        opponent_full_team: set[Pokemon] = battle_obj.teampreview_opponent_team
        opponent_mon: Optional[Pokemon] = battle_obj.opponent_active_pokemon
        if (opponent_mon != None):
            print()
            print(battle_obj.opponent_team)
            print(battle_obj.opponent_active_pokemon)
            print([str(mon.species) + ": " + str([typ for typ in mon.types]) for mon in battle_obj.teampreview_opponent_team])
            # Get list of all my current moves
            available_moves: dict[str, Move] = battle_obj.active_pokemon.moves
            battle_obj.available_moves
            for move in available_moves.values():
                print(str(move) + ", " + str(move.type) +  ": " + str(opponent_mon.damage_multiplier(move.type)))
            
            
            
        return self.choose_random_move(battle)
    
    def estimate_damage(self, opponent: Pokemon, move: Move) -> float:
        