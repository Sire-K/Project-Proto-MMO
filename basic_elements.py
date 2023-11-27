class Player:
    def __init__(self, name, score, health):
        self.name = name
        self.score = score
        self.health = health
        self.eliminated = False
        self.skill1_cooldown = 0
        self.skill2_cooldown = 0
        self.skill3_cooldown = 0

    def attack(self, target, skill_level):
        if skill_level == 1 and self.skill1_cooldown == 0:
            damage = 5
            self.skill1_cooldown = 0
            print(f"{self.name} used Skill 1 for {damage} damage.")
        elif skill_level == 2 and self.skill2_cooldown == 0:
            damage = 10
            self.skill2_cooldown = 1
            print(f"{self.name} used Skill 2 for {damage} damage.")
        elif skill_level == 3 and self.skill3_cooldown == 0:
            damage = 15
            self.skill3_cooldown = 2
            print(f"{self.name} used Skill 3 for {damage} damage.")
        else:
            print(f"{self.name} tried an invalid skill or it's on cooldown.")
            return

        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.eliminated = True
            print(f"{self.name} has been eliminated!")

    def choose_skill(self, skill_level):
        if skill_level == 1 and self.skill1_cooldown == 0:
            damage = 5
            print(f"{self.name} used Skill 1 for {damage} damage.")
        elif skill_level == 2 and self.skill2_cooldown == 0:
            damage = 10
            print(f"{self.name} used Skill 2 for {damage} damage.")
        elif skill_level == 3 and self.skill3_cooldown == 0:
            damage = 15
            print(f"{self.name} used Skill 3 for {damage} damage.")
        else:
            print(f"{self.name} tried an invalid skill or it's on cooldown.")
    
    def skill_cooldown(player, skill_level):
        if skill_level == 1:
            player.skill1_cooldown = 0  # skill1 has no cooldown
        elif skill_level == 2:
            player.skill2_cooldown = 1  # Cooldown of 1 turn for skill2
        elif skill_level == 3:
            player.skill3_cooldown = 2  # Cooldown of 2 turns for skill3
        else:
            print("Invalid skill level.")


def create_players(num_players):
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Enter the name for Player {i}: ")
        player = Player(name, 0, 100)  # Starting with 100 health
        players.append(player)
    return players
