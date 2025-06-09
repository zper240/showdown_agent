import random
from collections import defaultdict
from typing import List, Dict, Tuple, Set


class Player:
    def __init__(self, id: int):
        self.id = id
        self.wins = 0
        self.losses = 0
        self.history: Set[int] = set()

    def is_active(self, win_cap: int, loss_cap: int) -> bool:
        return self.wins < win_cap and self.losses < loss_cap

    def __repr__(self):
        return f"Player({self.id}, W:{self.wins}, L:{self.losses})"

    def reset(self):
        self.wins = 0
        self.losses = 0
        self.history.clear()


def simulate_match(p1: Player, p2: Player) -> Tuple[Player, Player]:
    winner = random.choice([p1, p2])
    loser = p2 if winner == p1 else p1
    winner.wins += 1
    loser.losses += 1
    p1.history.add(p2.id)
    p2.history.add(p1.id)
    return winner, loser


def run_tournament(players: list[Player], win_cap: int = 3, loss_cap: int = 2):
    round_num = 0

    print(
        f"🏆 Starting tournament with {len(players)} players (Win cap: {win_cap}, Loss cap: {loss_cap})"
    )

    for p in players:
        p.reset()

    while True:
        # Get active players
        active_players = [p for p in players if p.is_active(win_cap, loss_cap)]
        if len(active_players) < 2:
            break

        round_num += 1
        print(f"\n--- Round {round_num} ---")

        # Group players by (wins, losses)
        brackets: Dict[Tuple[int, int], List[Player]] = defaultdict(list)
        for p in active_players:
            brackets[(p.wins, p.losses)].append(p)

        for group_key in sorted(brackets.keys()):
            group = brackets[group_key]
            random.shuffle(group)
            unpaired = group[:]
            while len(unpaired) >= 2:
                p1 = unpaired.pop(0)
                # Find first player p2 not already played against p1
                for i, p2 in enumerate(unpaired):
                    if p2.id not in p1.history:
                        unpaired.pop(i)
                        winner, loser = simulate_match(p1, p2)
                        print(
                            f"Group {group_key}: {p1.id} vs {p2.id} → Winner: {winner.id}"
                        )
                        break
                else:
                    # No unique opponent available — just pair with next
                    p2 = unpaired.pop(0)
                    winner, loser = simulate_match(p1, p2)
                    print(
                        f"Group {group_key} (re-pair): {p1.id} vs {p2.id} → Winner: {winner.id}"
                    )

            # Bye if odd number
            if unpaired:
                bye_player = unpaired.pop()
                bye_player.wins += 1
                print(f"Group {group_key}: Player {bye_player.id} receives a BYE")

    print("\n🏁 Final Results:")
    final_sorted = sorted(players, key=lambda p: (-p.wins, p.losses, p.id))
    for p in final_sorted:
        status = (
            "✓ Qualified"
            if p.wins >= win_cap
            else ("✗ Eliminated" if p.losses >= loss_cap else "")
        )
        print(f"Player {p.id:3d} | W: {p.wins}, L: {p.losses} {status}")

    return [p for p in final_sorted if p.wins >= win_cap]


def main():
    n_players = 128

    players = [Player(i) for i in range(n_players)]
    players = run_tournament(players, win_cap=3, loss_cap=3)  # 64

    players = run_tournament(players, win_cap=3, loss_cap=3)  # 32

    players = run_tournament(players, win_cap=3, loss_cap=3)  # 16

    print("\n🏆 Tournament Summary:")
    for p in players:
        print(f"Player {p.id:3d} | W: {p.wins}, L: {p.losses}")


# Example usage
if __name__ == "__main__":
    main()
