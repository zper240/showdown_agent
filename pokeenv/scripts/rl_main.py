import numpy as np
from gymnasium.spaces import Box
from poke_env.player.singles_env import SinglesEnv
from poke_env.environment import AbstractBattle
from generic.max_damage import CustomAgent

from poke_env.data import GenData
from poke_env import AccountConfiguration

from poke_env.player.battle_order import (
    BattleOrder,
    DefaultBattleOrder,
    ForfeitBattleOrder,
)

from generic.max_damage import CustomAgent

team_one = """
Goodra (M) @ Assault Vest
Ability: Sap Sipper
EVs: 248 HP / 252 SpA / 8 Spe
Modest Nature
IVs: 0 Atk
- Dragon Pulse
- Flamethrower
- Sludge Wave
- Thunderbolt

Sylveon (M) @ Leftovers
Ability: Pixilate
EVs: 248 HP / 244 Def / 16 SpD
Calm Nature
IVs: 0 Atk
- Hyper Voice
- Mystical Fire
- Protect
- Wish

Cinderace (M) @ Life Orb
Ability: Blaze
EVs: 252 Atk / 4 SpD / 252 Spe
Jolly Nature
- Pyro Ball
- Sucker Punch
- U-turn
- High Jump Kick

Toxtricity (M) @ Throat Spray
Ability: Punk Rock
EVs: 4 Atk / 252 SpA / 252 Spe
Rash Nature
- Overdrive
- Boomburst
- Shift Gear
- Fire Punch

Seismitoad (M) @ Leftovers
Ability: Water Absorb
EVs: 252 HP / 252 Def / 4 SpD
Relaxed Nature
- Stealth Rock
- Scald
- Earthquake
- Toxic

Corviknight (M) @ Leftovers
Ability: Pressure
EVs: 248 HP / 80 SpD / 180 Spe
Impish Nature
- Defog
- Brave Bird
- Roost
- U-turn
"""


class SimpleRLPlayer(SinglesEnv):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        low = [-1, -1, -1, -1, 0, 0, 0, 0, 0, 0]
        high = [3, 3, 3, 3, 4, 4, 4, 4, 1, 1]
        self.observation_spaces = {
            agent: Box(
                np.array(low, dtype=np.float32),
                np.array(high, dtype=np.float32),
                dtype=np.float32,
            )
            for agent in self.possible_agents
        }

    def state(self) -> np.ndarray:
        return np.asanyarray([])

    def calc_reward(self, battle) -> float:
        return self.reward_computing_helper(
            battle, fainted_value=2.0, hp_value=1.0, victory_value=30.0
        )

    def embed_battle(self, battle: AbstractBattle):
        # -1 indicates that the move does not have a base power
        # or is not available

        moves_base_power = -np.ones(4)
        moves_dmg_multiplier = np.ones(4)
        for i, move in enumerate(battle.available_moves):
            moves_base_power[i] = (
                move.base_power / 100
            )  # Simple rescaling to facilitate learning

            if move.type:
                type_chart = GenData.from_gen(8).type_chart
                if battle.opponent_active_pokemon is not None:
                    moves_dmg_multiplier[i] = move.type.damage_multiplier(
                        battle.opponent_active_pokemon.type_1,
                        battle.opponent_active_pokemon.type_2,
                        type_chart=type_chart,
                    )

        # We count how many pokemons have fainted in each team
        fainted_mon_team = len([mon for mon in battle.team.values() if mon.fainted]) / 6
        fainted_mon_opponent = (
            len([mon for mon in battle.opponent_team.values() if mon.fainted]) / 6
        )

        # Final vector with 10 components
        final_vector = np.concatenate(
            [
                # moves_base_power,
                # moves_dmg_multiplier,
                [fainted_mon_team, fainted_mon_opponent],
            ]
        )
        return np.float32(final_vector)


account_one = "battle_one"
account_config_one = AccountConfiguration(account_one, None)

account_two = "battle_two"
account_config_two = AccountConfiguration(account_two, None)

player_config = AccountConfiguration("player", None)

test_env = SimpleRLPlayer(
    account_configuration1=account_config_one,
    account_configuration2=account_config_two,
    battle_format="gen9anythinggoes",
    team=team_one,
    start_challenging=True,
)

agent = CustomAgent(
    team="", account_configuration=player_config, battle_format="gen9anythinggoes"
)

data = test_env.reset()
print(data)

done = False
while not done:
    one = agent.choose_move(test_env.battle1)
    two = agent.choose_move(test_env.battle2)

    one = test_env.order_to_action(one, test_env.battle1)
    two = test_env.order_to_action(two, test_env.battle2)

    action = {account_one: one, account_two: two}
    observations, reward, done, truncated, info = test_env.step(action)
    print(observations)
    print(done)

    done = done[account_one] or done[account_two]

    print(done)
