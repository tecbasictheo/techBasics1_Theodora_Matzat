# I decided to improve my game and make the code clearer in structure.

import time
from os.path import exists

# variable
game_scene = 0

# function
def dead_restart(name):
    if not name:
        name = "Unknown Hero"
    time.sleep(1)
    print("...")
    time.sleep(4)
    print(f"Your character {name} is dead.")
    time.sleep(1)
    print("Try again ;)")
    exit()


def finished_game():
    print("You made it :) ")
    print("Good Job!")
    exit()


def step_one(game_scene):
    print("You are in a long corridor, you see no end")
    steps = input("How many steps do you wanna take? (Please type in numbers)")
    steps = int(steps)

    if 20 <= steps < 70:
        print("You walk beside a door, that you did not see from the entrance.")
        time.sleep(1)
        print("You decide to take your chance.")
        return 2
    elif steps < 20:
        print("You walk along the corridor")
        time.sleep(1)
        print("...")
        return game_scene
    else:
        print("You walk along the corridor and see no end.")
        print("Please try again.")
        return game_scene


def step_two(game_scene):
    steps2 = input("How many steps do you wanna take? (Please type in numbers)")
    steps2 = int(steps2)
    if steps2 == 0:
        print("You stand in place")
        time.sleep(1)
        print("...")
        print("Wanna try again?")
        return game_scene
    elif 20 <= steps2 < 70:
        print("You walk beside a door, that you did not see from the entrance.")
        time.sleep(1)
        print("You decide to take your chance.")
        return 9
    elif steps2 < 20:
        print("You walk along the corridor")
        time.sleep(1)
        print("...")
        return game_scene
    else:
        print("You walk along the corridor and see no end.")
        print("Please try again.")
        time.sleep(1)
        return game_scene


def questions(game_scene):
    frage1 = input("What is the answer to the Ultimate Question of Life, the Universe, and Everything?")
    frage1 = str(frage1)
    if frage1 == "42":
        print("Correct")
        return 6
    else:
        print("No")
        return game_scene


# wakeup room -
print("You are opening your eyes.")
time.sleep(1)
print("You are in the darkness. It is a small room. ")
time.sleep(1)
print("You try to make out any forms in the darkness, as your turn your head...")
print("You see something move...")
time.sleep(2)
print('"hello?"')
time.sleep(1)
print("...")
print('"You are finally awake."')
time.sleep(1)
print("...")
time.sleep(1)
name = input('"Whats your name?" ->')
time.sleep(1)
print('"hello', name, '"')
time.sleep(1)
print('"Behind you, there is a door. It just leads to another empty room."')
time.sleep(3)
print("You stand up and move towards the said direction")
print("...")
print('"Can I join you?"')
time.sleep(1)

# decision
while game_scene == 0:
    decision = input("Can they join you? (Yes or No)")
    if decision == "yes" or decision == "Yes":
        print('"Oh, thank god. Can you help me up?"')
        time.sleep(1)
        print("You move towards the voice and take their reaching hand, to pull them up.")
        print("Even though your eyes are getting adjusted to the dark, you still see just the body outlines")
        time.sleep(5)
        print("They move fast to the said door, you rush after. Unsure if them joining you was the right decision")
        time.sleep(5)
        print(
            "They reach the said door. Opening it without hesitation, you step right behind them through. Scared to be shut in.")
        time.sleep(5)
        print("The door closes behind you and you hear the door lock")
        time.sleep(2)
        print("You reach for the door, but do not find a handle")
        time.sleep(2)
        print('"There is no way back..."')
        print('"We have here to doors, lets take each one and take a look"')
        while game_scene == 0:
            door = input('"Which one do you want? Right or left?"')
            if door == "left" or door == "Left":
                print('"You take the right door and I the other one"')
                game_scene = step_one(game_scene)
            elif door == "right" or door == "Right":
                print('"You take the left door and I the other one"')
                game_scene = 2
            else:
                print("Value not valid, please try again")

    elif decision == "no" or decision == "No":
        print("...")
        time.sleep(1)
        print(
            "You hear something move closer. Thinking they are coming for you makes you move backwards, until you feel the wooden door.")
        time.sleep(1)
        print("As your hear them coming closer, you do not think and just open the door behind you")
        print("You rush trough the door and shut it close")
        time.sleep(2)
        print("...")
        print("The new room is dimly lit.")
        time.sleep(1)
        print("As you look around the new room you only see two doors across the room, other ways the room is empty")
        game_scene = 7
        while game_scene == 7:
            doorone = input("Which one do you want? Right or left?")
            if doorone == "left" or doorone == "Left":
                print("You take the left door")
                game_scene = step_one(game_scene)
            elif doorone == "right" or doorone == "Right":
                print("You take the right door")
                game_scene = 2
            else:
                print("Value not valid, please try again")
    else:
        print("Value not valid, please try again")

# Question room
while game_scene == 2:
    time.sleep(1)
    print("You open the door in front of you and step through.")
    time.sleep(1)
    print("You try to hold the door open, but it is to heavy and shuts close behind you")
    time.sleep(3)
    print('"Shit"')
    time.sleep(1)
    print("You look around and move towards the center of the room.")
    print("It has a small pedestal in the middle and two doors across the room.")
    time.sleep(1)
    print("You move slowly towards the pedestal.")
    time.sleep(2)
    print("""There is something written
    ...""")
    time.sleep(1)
    game_scene = questions(game_scene)

while game_scene == 6:
    print("You here the doors click, they may be open now")
    time.sleep(2)
    doortwo = input("What door do you wanna choose? (Left or Right)")
    if doortwo == "left" or doortwo == "Left":
        print("You take the left door")
        print("You step through the door in the darkness")
        game_scene = step_two(game_scene)
    elif doortwo == "right" or doortwo == "Right":
        print("You take the right door")
        time.sleep(1)
        print("You are in a long corridor, you see no end")
        dead_restart()
    else:
        print("Value not valid, please try again")

# last door room
while game_scene == 9:
    lastdoor = input("Do you wanna go through the door? (Yes or No)")
    if lastdoor == "yes" or lastdoor == "Yes":
        print("You step through the door")
        time.sleep(2)
        print("You are blended by the light")
        time.sleep(2)
        finished_game()
    elif lastdoor == "no" or lastdoor == "NO":
        print("You pass the door")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("You continue into the darkness")
        time.sleep(3)
        print("You are lost forever...")
        dead_restart(name)
    else:
        print("Value not valid, please try again")
