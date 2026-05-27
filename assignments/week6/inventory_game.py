# --- A grocery shopping experience---
# I added expectipn on the functions, so that in the game the player knows it wasnt an Input error

import csv

# All the used lists:
home = []
shopping_card = []
Aisle_1 = [
    {"name": "Apple", "type": "fruit", "description": "Can be eaten as a snack or made into something like a tarte."},
    {"name": "Banana", "type": "fruit", "description": "Can be eaten as snack or used as egg replacement for backing."},
    {"name": "Melon", "type": "fruit", "description": "Sweet and in the moment in season."},
    {"name": "Tomato", "type": "vegetable", "description": "Good for sauce and salats."},
    {"name": "Garlic", "type": "vegetable", "description": "Good seasoning."},
    {"name": "Potatoes", "type": "vegetable", "description": "A stable for every meal"}
]
Aisle_2 = [
    {"name": "Water", "type": "drink", "description": "Good for drinking and cooking."},
    {"name": "Milk", "type": "drink", "description": "For drinking, cooking and backing"},
    {"name": "Oat-milk", "type": "drink", "description": "An vegan alternative to milk"}
]
Aisle_3 = [
    {"name": "Cheese", "type": "cooled food", "description": "Its not vegan."},
    {"name": "Tofu", "type": "cooled food", "description": "A protein-source."}
]
Aisle_4 = [
    {"name": "Rice", "type": "food", "description": "A grain, a stable for warm meals."},
    {"name": "Noodles", "type": "food", "description": "Can be vegan, you are unsure."},
    {"name": "Bread", "type": "food", "description": "A stable for every meal, can be vegan."}
]

Grocery_store = [Aisle_1, Aisle_2, Aisle_3, Aisle_4]
# My constants
MAX_CARD_SIZE = 5

DEBUG = True


# --- Functions ---
def show_card():
    if not shopping_card:
        print("Card is empty")
    else:
        for d in shopping_card:
            print(d["name"])


def show_home():
    if not home:
        print("You did not buy anything")
    else:
        for d in home:
            print(d["name"])


def show_aisle_items_1():
    for d in Aisle_1:
        print(d["name"])


def show_aisle_items_2():
    for d in Aisle_2:
        print(d["name"])


def show_aisle_items_3():
    for d in Aisle_3:
        print(d["name"])


def show_aisle_items_4():
    for d in Aisle_4:
        print(d["name"])


def pick_up(item_name):
    try:
        item_name = item_name.strip().strip("[]")
        if MAX_CARD_SIZE >= len(shopping_card):
            if item_name not in [item["name"] for item in shopping_card]:  # not mine
                for aisle in Grocery_store:
                    for item in aisle:
                        if item["name"].lower() == item_name.lower():
                            aisle.remove(item)
                            shopping_card.append(item)
                            print(f"You picked up the {item['name']}")
                            return shopping_card
                print(f"There is no '{item_name}' in the store.")
                return shopping_card
            else:
                print("You already picked up the " + item_name + ".")
                return shopping_card
        else:
            print("Not enough space in inventory")
            return shopping_card
    except:
        print("An exception occurred")



def drop(item_name):
    item_name = item_name.strip().strip("[]")
    if item_name in [item["name"].lower() for item in shopping_card]:
        try:
            if item_name == "fruit" or "vegetable":
                for item in shopping_card:
                    shopping_card.remove(item)
                    Aisle_1.append(item)
                    print("You put " + item_name + " back.")
                return shopping_card
            elif item_name == "drink":
                for item in shopping_card:
                    shopping_card.remove(item)
                    Aisle_2.append(item)
                    print("You put " + item_name + " back.")
                return shopping_card
            elif item_name == "cooled food":
                for item in shopping_card:
                    shopping_card.remove(item)
                    Aisle_3.append(item)
                    print("You put " + item_name + " back.")
                return shopping_card
            elif item_name == "food":
                for item in shopping_card:
                    shopping_card.remove(item)
                    Aisle_4.append(item)
                    print("You put " + item_name + " back.")
                return shopping_card
            else:
                print("This item does not exist.")
               return shopping_card

        except:
            print("An exception occurred")

    else:
        return shopping_card


def buy(item_name):
    item_name = item_name.strip().strip("[]")
    try:
        for item in shopping_card:
            if item["type"] == "food":
                if item["name"].lower() == item_name.lower():
                    print("You found something for the main course.")
                    input("Are your sure it is vegan?")
                    if input == "YES" or "yes":
                        shopping_card.remove(item)
                        home.append(item)
                        print("You bought it")
                        return shopping_card
                    else:
                        shopping_card.remove(item)
                        Aisle_4.append(item)
                        print(f"You put, {item_name}, away.")
                        return shopping_card
            elif item["type"] == "drink":
                if item["name"].lower() == item_name.lower():
                    print("You found something to drink.")
                    input("Are your sure it is vegan?")
                    if input == "YES" or "yes":
                        shopping_card.remove(item)
                        home.append(item)
                        return shopping_card
                    else:
                        shopping_card.remove(item)
                        Aisle_2.append(item)
                        print(f"You put, {item_name}, away.")
                        return shopping_card
            elif item["type"] == "vegetable" or "fruit":
                if item["name"].lower() == item_name.lower():
                    input("Are your sure that you want to buy it?")
                    if input == "YES" or "yes":
                        shopping_card.remove(item)
                        home.append(item)
                        return shopping_card
                    else:
                        shopping_card.remove(item)
                        Aisle_1.append(item)
                        print(f"You put, {item_name}, away.")
                    return shopping_card
            elif item["type"] == "cooled food":
                if item["name"].lower() == item_name.lower():
                    print("You found something for the main course.")
                    input("Are your sure it is vegan?")
                    if input == "YES" or "yes":
                        shopping_card.remove(item)
                        home.append(item)
                        return shopping_card
                    else:
                        shopping_card.remove(item)
                        Aisle_3.append(item)
                        print(f"You put, {item_name}, away.")
                        return shopping_card
    except:
        print(f"You do not have this, {item_name}, in your inventory.")
        return shopping_card


def examine(item_name):  # works
    try:
        for item in shopping_card:
            print(f"Name: {item['name']}")
            print(f"Type: {item['type']}")
            print(f"Description: {item['description']}")
            return
    except:
            print(f"You do not have this, {item_name}, in your inventory.")
            return


def end_game():
    if len(home) == 6:
        print("You bought all items for the dinner.")
        print("Thanks for playing!")
        exit()


def save_file():
    with open("inventory.csv", "w") as file:
        writer = csv.writer(file)

# --- Game Loop ---

def game_loop():
    print("Welcome to the Grocery shopping Game!")
    print("You are going shopping for a dinner with your vegan child.")
    print("Be careful, you cannot carry more than five items!")
    print("Type 'help' for a list of commands.")

    end_game()
    while True:
        command = input("\n> ").strip().lower()

        match command.split():  # is there a way to do grammar correction like if item["name"].lower() == item_name.lower() and for spaces?
            case ["help"]:
                print(
                    "Commands: shoppingcard, home, look-aisle1, look-aisle2, look-aisle3, look-aisle4, pickup [item], drop [item], buy [item], examine [item], quit")
            case ["shoppingcard"]:
                show_card()
            case ["home"]:
                show_home()
            case ["look-aisle1"]:
                show_aisle_items_1()
            case ["look-aisle2"]:
                show_aisle_items_2()
            case ["look-aisle3"]:
                show_aisle_items_3()
            case ["look-aisle4"]:
                show_aisle_items_4()
            case ["pickup", item_name]:
                pick_up(item_name)
            case ["drop", item_name]:
                drop(item_name)
            case ["buy", item_name]:
                buy(item_name)
            case ["examine", item_name]:
                examine(item_name)
            case ["quit"]:
                print("Thanks for playing!")
                break
            case _:
                print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    game_loop()
    save_file()
