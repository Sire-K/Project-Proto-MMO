def player_turn(player, opponents):
    print(f"{player.name}'s turn:")
    print("1. Attack")
    print("2. Use Skill")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if choice == 1:
        target_index = int(input("Enter the index of the player to attack: "))
        if 0 <= target_index < len(opponents):
            player.attack(opponents[target_index])
        else:
            print("Invalid target index.")
    elif choice == 2:
        skill_level = int(input("Choose skill level (1-3): "))
        player.choose_skill(skill_level)
    else:
        print("Invalid choice.")