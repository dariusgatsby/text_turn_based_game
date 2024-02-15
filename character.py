import math
class ClassType:
    def __init__(self) -> None:
        self.health = None
        self.attack_stat = None
        self.stamina = None
        self.speed = None
        

    def warrior(self):
        self.class_name = "Warrior"
        self.health = 150
        self.stamina = 125
        self.speed = 75
        self.attack_stat = 30

    def thief(self):
        self.class_name = "Thief"
        self.health = 100
        self.stamina = 200
        self.speed = 150
        self.attack_stat = 20

    def knight(self):
        self.class_name = "Knight"
        self.health = 200
        self.stamina = 150
        self.speed = 50
        self.attack_stat = 40

    def skeleton(self):
        self.class_name = "Skeleton"
        self.health = 100
        self.stamina = 200
        self.speed = 100
        self.attack_stat = 20

    def goblin(self):
        self.class_name = "Goblin"
        self.health = 150
        self.stamina = 175
        self.speed = 80
        self.attack_stat = 25

class Character(ClassType):
    def __init__(self, name: str, class_type=None) -> None:
        super().__init__()
        self.name = name
        self.type = class_type
        self.level = 1
        self.heals = 5

    def attack(self):
        damage = self.attack_stat - (self.stamina / 2) * (self.level / 50)
        self.stamina -= 15
        return damage
    
    def take_damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.death()

    def rest(self):
        self.stamina += 20
        return self.stamina
    
    def heal_self(self):
        if self.heals == 0:
            print("No more heals")
            return None
        else:
            self.health += 25
            self.heals -= 1
            math.ceil(self.health)
        message = f"Health is now {self.health}, {self.heals} heals left."
        return message

    def death(self):
        death_message = f"{self.name} DIED!"
        print(death_message)
        return None