from basic_elements import Player, create_players
from fight_simulation import simulate_fight
from health import display_health, take_damage
from turns_and_skills import player_turn
from elemination_bracket import display_elimination_bracket

def main():
    num_players = int(input("Enter the number of players: "))
    players = create_players(num_players)

    while len(players) > 1:
        for player in players:
            if not player.eliminated:
                display_health(players)
                player_turn(player, [opponent for opponent in players if opponent != player and not opponent.eliminated])

        # Simulate fights between remaining players
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                if not players[i].eliminated and not players[j].eliminated:
                    simulate_fight(players[i], players[j])

        # Remove eliminated players
        players = [player for player in players if not player.eliminated]

    # Display the winner
    print(f"{players[0].name} is the winner!")

if __name__ == "__main__":
    main()
