# adventure game
import time
import random


def print_pause(s):
    print(s)
    time.sleep(.5)


def intro():
    creature = random.choice(["dragon", "suspicious shadow",
                              "big and evil strawberry"])
    scenario = random.choice(["a forest", "an old stadium", "an unknown park",
                              "nowhere"])
    print_pause(f"You woke up in the middle of {scenario}!")
    print_pause("Someone said: 'I was waiting for you!'")
    print_pause("You don't know who's there...")
    print_pause(f"Suddenly, you see a {creature}!")
    print_pause("You are so scared! You only have one book in your hands.")
    print_pause("You see a big rock where you can hide "
                "and a door behind some trees.")


def play(weapon):
    to_do = input("What do you want to do?\n"
                  "1 Hide behind a big rock\n"
                  "2 Knock the mysterious door\n"
                  "(Please enter 1 or 2)\n")
    if "1" == to_do:
        hide(weapon)
    elif "2" == to_do:
        door(weapon)
    else:
        print_pause("Sorry, I don't understand.")
        play(weapon)


def hide(weapon):
    if 'blue light' in weapon:
        print_pause("You see a giant green snail again, but you already have "
                    "the blue light of power!")
        print_pause("A light shines very brightly.")
        print_pause("You see yourself at the crossroads again.")
        play(weapon)
    else:
        print_pause("You are behind a big rock.")
        print_pause("You see a giant green snail next to you.")
        print_pause("This giant snail is offering something weird. "
                    "You are fiding it strange, you cannot see well.")
        get_answer(weapon)


def get_answer(weapon):
    answer = input("Will you accept? (yes or no)\n").lower()
    if 'yes' == answer:
        yes_answer(weapon)
    elif 'no' == answer:
        no_answer(weapon)
    else:
        print_pause("Sorry, I don't understand.")
        get_answer(weapon)


def yes_answer(weapon):
    print_pause("A giant green snail touched your book. "
                "The book absorbed a bright light.")
    print_pause("You opened your book and pulled out a blue "
                "light of power from inside it.")
    weapon.append('blue light')
    print_pause("You see yourself at the crossroads again.")
    play(weapon)


def no_answer(weapon):
    print_pause("You were afraid of a giant green snail and ran away "
                "as fast as you can.")
    print_pause("You see yourself at the crossroads again.")
    play(weapon)


def door(weapon):
    print_pause("The creature opens the door and appears in front of you!")
    get_response(weapon)


def get_response(weapon):
    response = input("You can run or fight. What do you want to do?\n"
                     "1 Run\n"
                     "2 Fight\n"
                     "(Please enter 1 or 2)\n")
    if '1' == response:
        one_response(weapon)
    elif '2' == response:
        two_response(weapon)
    else:
        print_pause("Sorry, I don't understand.")
        door(weapon)


def one_response(weapon):
    if 'blue light' in weapon:
        print_pause("You try to run but where can you go?")
        print_pause("You see yourself at the crossroads again.")
        play(weapon)
    else:
        print_pause("You try to run, but where can you go?")
        print_pause("You see yourself at the crossroads again.")
        play(weapon)


def two_response(weapon):
    if 'blue light' in weapon:
        print_pause("Wonderful! You have the power of blue light!")
        print_pause("You are saved and woke up in the real world!")
        print_pause("You won!")
        play_again(weapon)
    else:
        print_pause("You only have one book in your hands.")
        print_pause("You try to fight, but you cannot win. "
                    "Sorry, I know that you did your best.")
        print_pause("Game over!")
        play_again(weapon)


def play_again(weapon):
    again = input("Would you like to play again? (yes/no)?\n").lower()
    if again == "yes":
        start_game()
    elif again == "no":
        print_pause("Okay! Have a nice day!")
    else:
        print_pause("Sorry, I don't understand.")
        play_again(weapon)


def start_game():
    weapon = []
    intro()
    play(weapon)


start_game()
