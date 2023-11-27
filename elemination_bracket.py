def display_elimination_bracket(players):
    eliminated_players = [player for player in players if player.eliminated]
    print("Eliminated players:")
    for player in eliminated_players:
        print(player.name)
