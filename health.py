def display_health(players):
    for player in players:
        print(f"{player.name} - Health: {player.health}")

def take_damage(player, damage):
    player.health -= damage
    if player.health <= 0:
        player.eliminated = True
        print(f"{player.name} has been eliminated!")