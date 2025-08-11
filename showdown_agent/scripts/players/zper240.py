from poke_env.battle import AbstractBattle
from poke_env.player import Player

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
        return self.choose_random_move(battle)
