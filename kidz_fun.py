def welcome():
    print("Welcome to the Kidz Fun Holiday Programme")


fun_roll = []
fun_ages = []

active_roll = []
active_ages = []


def drop_off():
    print("--------------------------------------------------")
    print("Dropping off a child")
    choice = input("Which holiday programme is your child attending: \n f for Fun in the Sun, \n a for Active Kidz \n >>> ").lower()
    while choice != "f" and choice != "a":
        choice = input("That is an invalid input. \nWhich holiday programme is your child attending: \n f for Fun in the Sun, \n a for Active Kidz \n >>> ").lower()

    name = input("What is your child's name >>> ").capitalize()
    age = int(input(f"How old is {name} >>> "))

    if choice == "f":
        fun_roll.append(name)
        fun_ages.append(age)
    elif choice == "a":
        active_roll.append(name)
        active_ages.append(age)

    print(f"{name} added to {choice.upper()}")
    ask_user()


def ask_user():
    print("=================================================")
    print("You have three options: \n d to drop off a child, \n x to calculate the average age, \n quit to exit the program")
    choice = input("What would you like to do >>> ").lower()
    while choice != "d" and choice != "x" and choice != "quit":
        choice = input("Invalid input. What would you like to do >>> ").lower()

    if choice == "d":
        drop_off()

    elif choice == "x":
        print(f"The average age of the {len(fun_roll)} children in the Fun in the Sun programme is {calc_avg(fun_ages, fun_roll)}")
        print(f"The average age of the {len(active_roll)} children in the Active Kidz programme is {calc_avg(active_ages, active_roll)}")

        ask_user()

    else:
        print("Goodbye")


def calc_avg(ages, roll):
    total_ages = sum(ages)
    total_children = len(roll)
    if total_ages == 0 or total_children == 0:
        return 0
    return round(total_ages / total_children)

# main routine


welcome()
ask_user()



