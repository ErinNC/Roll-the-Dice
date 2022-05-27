"""This Python-based application runs a simulation of rolling up to six dice. 
Each die is six-sided. After each roll, an ASCII diagram will be generated to
display the dice faces.
"""


# Import random module for roll_dice()
import random


# ----------------------- Dice art to display -----------------------

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    )
}

die_height = len(dice_art[1])
die_width = len(dice_art[1][0])
die_separator = " "


# -------------------- Functions created for app --------------------

def validate_input(dice_roll_input):
    """Return user input as an integer between 1 and 6 (inclusive).

    Check if 'dice_roll_input' is from 1 to 6. If so, return the user input
    as an integer.

    If user input is not an integer from 1 to 6, raise an error and tell
    the user to enter a valid number.
    """

    
    if dice_roll_input.strip() in ["1", "2", "3", "4", "5", "6"]:
        return int(dice_roll_input)
    else:
        print("Invalid input. Please restart app and enter a number 1 to 6.")
        raise SystemExit(1)


def roll_dice(dice_roll):
    """Return a list of integers with length of the user input value.
    
    Each integer in returned list is a pseudo-random number from 1 to 6."""

    roll_results = []
    for _ in range(dice_roll):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results


def generate_dice_diagrams(roll_results):
    """Return an ASCII diagram of dice faces from 'roll_results'.

    The returned string contains representations of each die.
    Example: roll_results = [6,5,3,2] will look like this:

    ******************* RESULTS *******************
    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
    │  ●   ●  │ |  ●   ●  | |  ●      | |  ●      |
    │  ●   ●  │ |    ●    | |    ●    | |         |
    │  ●   ●  │ |  ●   ●  | |      ●  | |      ●  | 
    └─────────┘ └─────────┘ └─────────┘ └─────────┘
    """

    dice_faces = _get_dice_faces(roll_results)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "*")

    dice_diagrams = "\n".join([diagram_header] + dice_faces_rows)
    return dice_diagrams


def _get_dice_faces(roll_results):
    """Non-public function to generate a list of dice faces using dice_art"""
    dice_faces = []
    for value in roll_results:
        dice_faces.append(dice_art[value])
    return dice_faces


def _generate_dice_faces_rows(dice_faces):
    """Non-public function to generate a list containing the dice faces rows"""
    dice_faces_rows = []
    for row_index in range(die_height):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_index])
        row_string = die_separator.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows


# ------------------ Application's main code block ------------------

# 1. Prompt user to enter an integer 1-6 for how many dice to roll
dice_roll_input = input("How many dice would you like to roll? (1-6) ")

# 2. Validate user input
dice_roll = validate_input(dice_roll_input)

# 3. Roll the dice
roll_results = roll_dice(dice_roll)

# 4. Generate the ASCII diagrams for each die face
dice_face_diagram = generate_dice_diagrams(roll_results)

# 5. Display the diagram result of user input
print(f"\n{dice_face_diagram}")
