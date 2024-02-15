from character import Character
import random
import os

def clear():
    pass
    os.system("clear")

def player_move(choose_move):
    if choose_move == 1:
        print("You attacked!")
        damage = player1.attack()
        goblin.take_damage(damage)
        print(f"Goblin took {damage} damage!. Their health is now {goblin.health}!")
        print(f"Your stamina {player1.stamina}")
        # clear()
    elif choose_move == 2:
        # clear()
        player1.rest()
        print(f"You rested. Your stamina increased: {player1.stamina}")
    elif choose_move == 3:
        # clear()
        player1.heal_self()
        print(f"You healed. Your health increased: {player1.stamina}")

def enemy_move():
    rand_num = random.randint(0, 75)

    if rand_num <= 25:
        # clear()
        damage = goblin.attack()
        player1.take_damage(damage)
        print(f"You took {damage} damage! Your health is now {player1.health}!")
    elif 25 <= rand_num <= 50 and goblin.stamina < 150:
        # clear()
        goblin.rest()
        print("The goblin rested to regain it's stamina")
    elif rand_num > 50 and goblin.health > 160:
        print(f"{goblin.name} tried to heal but couldn't.")
    elif rand_num > 50 and goblin.health < 160:
        goblin.heal_self()
        print(f"{goblin.name} healed themselves!")
    

    else:
        # clear()
        pass
        
        print(f"{goblin.name} did nothing.")

choosing = True
while choosing:
    name_choice = input("Choose your name: ")
    class_choice = int(input("Choose your class (enter number): \n1.Warrior\n2.Thief\n3.Knight\nPick a class: "))

    player1 = Character(name_choice)

    if class_choice == 1:
        player1.warrior()
    elif class_choice == 2:
        player1.thief()
    elif class_choice == 3:
        player1.knight()
    else: 
        print("Choose a valid class")
        continue

    print(f"{player1.class_name} class has {player1.health} health \n{player1.attack_stat} attack stat \n{player1.stamina} stamina \n{player1.speed} speed. Continue? Y/N?")
    
    player_continue = input().capitalize()
    if player_continue == "Y":
        choosing = False
    if player_continue == "N":
        continue

alive = True


goblin = Character("Sir Gobs")
goblin.goblin()
clear()
print(f"Your opponent is {goblin.name}!")
while alive:
    
    
    print(f"{goblin.name} has Health: {goblin.health} Stamina: {goblin.stamina}")
    choose_move = input(f"Choose what to do! You have Health: {player1.health} Stamina: {player1.stamina} Heals Left: {player1.heals}\n1.Attack\n2.Rest\n3.Heal yourself\nChoose: ")

    player_move(int(choose_move))
    enemy_move()

    if player1.health < 0:
        player1.death()
        alive = False
    if goblin.health < 0:
        goblin.death()
        alive = False
    

    

    

    
    
    
