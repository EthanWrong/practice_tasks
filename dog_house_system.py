# By Ethan Wong
# 16 March 2022 10:10pm

"""
Possible Changes to make:
    make cancel operation a function:
        # cancel operation
        if new_dog == "/cancel":
            print(f" Pick up cancelled")
            print()
"""


def welcome():
    print("Welcome to Dog House, the system to keep \ntrack of all your dogs staying at *DogsRus*")


dog_house = ["Oliver"]


def drop_off():
    print("----")
    print("Dropping off dog: ")
    new_dog = input(" What is the name of your dog? >>> ").capitalize()

    # cancel operation
    if new_dog == "/cancel":
        print(f" Pick up cancelled")
        print()
        ask_user()
    while not duplicate_dog(new_dog):
        # cancel operation
        if new_dog == "/cancel":
            print(f" Drop off {new_dog} cancelled")
            print()
            ask_user()
            break

        new_dog = input(
            f"\n There is already a dog named {new_dog.capitalize()}, \n '/cancel' to cancel or \n please enter a new name or add a number >>> ").capitalize()

    if confirmed(f" Are you sure you want to register {new_dog}? y/n >>> "):
        dog_house.append(new_dog)
        print(f" {new_dog} has been registered")
    else:
        print(f" Registering {new_dog} has been cancelled")

    print()
    ask_user()


def pick_up():
    print("Picking up dog: ")
    dog = input(" What dog would you like to pick up? >>> ").capitalize()
    while not dog_exists(dog):
        # cancel operation
        if dog == "/cancel":
            print(f" Pick up {dog} cancelled")
            print()
            ask_user()
            break

        dog = input(
            f" There is no dog called {dog} in the Dog House currently, \n '/cancel' to cancel or \n please enter another dog >>> ").capitalize()

    if confirmed(f" Are you sure you want to pick up {dog}? y/n >>> "):
        dog_house.remove(dog)
        print(f" {dog} has been picked up")
    else:
        print(f" Pick up {dog} cancelled")

    print()
    ask_user()


daily_rate = 22.50
hourly_rate = 22.50 / 24


def calc_cost():
    print(f"Calculating Cost:")
    hours = int(input(f" How many hours will the dogs stay for >>> "))
    print()
    print(
        f" At the daily rate of ${daily_rate:.2f} per dog, the total cost for {len(dog_house)} dogs to stay {hours} hours, will be: \n == ${len(dog_house) * hours * hourly_rate:.2f}")
    print()
    input("Press Enter to confirm read >>> ")
    print()
    ask_user()


def print_roll():
    print("Printing roll:")
    print(" **************")
    for i in dog_house:
        print("  "+i)
    print(" **************")
    print()
    input("Press Enter to confirm read >>> ")
    ask_user()


def confirmed(message):
    confirm = ""
    while confirm != "Y" and confirm != "N" and confirm != "/cancel":
        confirm = input(message).capitalize()
    if confirm == "Y":
        return True
    else:
        return False


def dog_exists(dog):
    for i in dog_house:
        if i == dog:
            return True
    return False


def duplicate_dog(new_dog):
    for i in dog_house:
        if i == new_dog:
            return False
    return True


def quit_sys():
    print("Goodbye!")


def ask_user():
    print("=================================================")
    print("What would you like to do? Select one of the options below:")
    print(" ---")
    print("d - Drop off a dog")
    print("p - Pick up a dog")
    print("$ - Calculate cost")
    print("r - print the Roll")
    print("quit - Quit the system")
    print("/cancel - at any time to cancel current operation")
    print(" ---")

    choice = str(input("Please enter an option >>> "))
    while choice != "d" and choice != "p" and choice != "$" and choice != "r" and choice != "quit":
        choice = input("Please enter a valid option >>> ")

    if choice == "d":
        drop_off()
    elif choice == "p":
        pick_up()
    elif choice == "$":
        calc_cost()
    elif choice == "r":
        print_roll()
    elif choice == "quit":
        quit_sys()
    else:
        print("Unexpected input")


# main routine


welcome()
ask_user()
