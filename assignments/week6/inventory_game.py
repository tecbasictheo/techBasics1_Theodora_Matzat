# --- A grocery shopping experience---
# The functions function, but there is an error with the keys.

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
    {"name": "Bread", "type": "food", "description": "A stable for every meal, can be vegan."},
]
# My constants
MAX_CARD_SIZE = 5

# --- Functions ---
def show_card():
    if not shopping_card:
        print("Card is empty")
    else:
        for d in shopping_card:
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
    print(f"DEBUG: item_name = '{item_name}'")
    item_name = item_name.strip()
    if MAX_CARD_SIZE >= len(shopping_card):
        if item_name not in shopping_card:
            if item_name in Aisle_1:
                for item in Aisle_1:
                    if item["name"].lower() == item_name.lower():
                        Aisle_1.remove(item)
                        shopping_card.append(item)
                        print(f"You picked up the {item['name']}")
                return shopping_card
            elif item_name in Aisle_2:
                for item in Aisle_2:
                    if item["name"].lower() == item_name.lower():
                        Aisle_2.remove(item)
                        shopping_card.append(item)
                        print(f"You picked up the {item['name']}")
                return shopping_card
            elif item_name in Aisle_3:
                for item in Aisle_3:
                    if item["name"].lower() == item_name.lower():
                        Aisle_3.remove(item)
                        shopping_card.append(item)
                        print(f"You picked up the {item['name']}")
                return shopping_card
            elif item_name in Aisle_4:
                for item in Aisle_4:
                    if item["name"].lower() == item_name.lower():
                        Aisle_4.remove(item)
                        shopping_card.append(item)
                        print(f"You picked up the {item['name']}")
                return shopping_card
            else:
                print(f"There is no '{item_name}' in the store.")
                return shopping_card
        else:
            print("You already picked up the " + item_name + ".")
            return shopping_card
    else:
        print("Not enough space in inventory")
        return shopping_card

def drop(item_name):
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

def buy(item_name):
    if item_name in shopping_card:
        for item in shopping_card:
            if item == "food":
                print("You found something for the main course.")
                input("Are your sure it is vegan?")
                if input == "YES" or "yes":
                    shopping_card.remove(item)
                    home.append(item)
                    return shopping_card
                else:
                    shopping_card.remove(item)
                    Aisle_4.append(item)
                    print(f"You put, {item_name}, away.")
                    return shopping_card
            elif item == "drink":
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
            elif item == "vegetable" or "fruit":
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
            elif item == "cooled food":
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
        return home
    else:
        print(f"You do not have this, {item_name}, in your inventory.")
    return shopping_card

def examine(item_name):  # works
    for item in shopping_card:
        print(f"Name: {item['name']}")
        print(f"Type: {item['type']}")
        print(f"Description: {item['description']}")
        return
    else:
        print(f"You do not have this, {item_name}, in your inventory.")
        return

def end_game():
    if len(home) == 6:
        print("You bought all items for the dinner.")
        print("Thanks for playing!")
        exit()
# --- Game Loop ---

def game_loop():
    print("Welcome to the Grocery shopping Game!")
    print("You are going shopping for a dinner with your vegan child.")
    print("Be careful, you cannot carry more than five items!")
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        end_game()
        # As an example, here I used the match/case syntax to replace long if/else statements
        # This feature is only supported from Python 3.10 and above

        match command.split():
            case ["help"]:
                print("Commands: inventory, look Aisle 1, look Aisle 2, look Aisle 3, look Aisle 4, pickup [item], drop [item], use [item], examine [item], quit")
            case ["Shopping card"]:
                show_card()
            case ["look Aisle 1"]:
                show_aisle_items_1()
            case ["look Aisle 2"]:
                show_aisle_items_2()
            case["look Aisle 3"]:
                show_aisle_items_3()
            case ["look Aisle 4"]:
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
            case _:  # else
                print("Unknown command. Type 'help' to see available commands.")

if __name__ == "__main__":
    game_loop()
