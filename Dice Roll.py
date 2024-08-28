# import random
# define a function to roll dice
# create a dictionary that have the drawings of the dice

import random


def roll_dice():

    dice_faces = {
        1: (
            "┌─────┐",
            "│  1  │",
            "│  •  │",
            "│     │",
            "└─────┘",
        ),
        2: (
            "┌─────┐",
            "│•    │",
            "│  2  │",
            "│    •│",
            "└─────┘",
        ),
        3: (
            "┌─────┐",
            "│• 3  │",
            "│  •  │",
            "│    •│",
            "└─────┘",
        ),
        4: (
            "┌─────┐",
            "│•   •│",
            "│  4  │",
            "│•   •│",
            "└─────┘",
        ),
        5: (
            "┌─────┐",
            "│• 5 •│",
            "│  •  │",
            "│•   •│",
            "└─────┘",
        ),
        6: (
            "┌─────┐",
            "│•   •│",
            "│• 6 •│",
            "│•   •│",
            "└─────┘",
        ),
    }


    roll=input("Roll dice? (Yes/No): ")

    while roll.lower()=="Yes".lower():
        dice1=random.randint(1, 6)
        dice2=random.randint(1, 6)

        print("dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_faces[dice1]))
        print("\n".join(dice_faces[dice2]))

        roll=input("Roll again? (Yes/No): ")


while True:
    roll_dice()