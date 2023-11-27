def player_turn(player, opponents):
    print(f"{player.name}'s turn:")
    print("1. Attack")
    print("2. Use Skill")
    choice = int(input("Enter your choice: "))
    
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

def skill_cooldown(player, skill_level):
    def skill_cooldown(player, skill_level):
        if skill_level == 1:
            player.skill1_cooldown = 0  # Assuming skill1 has no cooldown
        elif skill_level == 2:
            player.skill2_cooldown = 1  # Cooldown of 1 turn for skill2
        elif skill_level == 3:
            player.skill3_cooldown = 2  # Cooldown of 2 turns for skill3
        else:
            print("Invalid skill level.")
        pass
