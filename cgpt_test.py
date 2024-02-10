import random


def roll_dice(num_sides, num_rolls):
    """
    This function simulates rolling a dice with a given number of sides a specified number of times and returns a list of the individual rolls, as well as their total sum.
    """
    rolls = []
    total_sum = 0
    for i in range(num_rolls):
        dice_roll = random.randint(1, num_sides)
        rolls.append(dice_roll)
        total_sum += dice_roll
    return rolls, total_sum


# Ask user for number of sides on the dice
num_sides = int(input("How many sides does the dice have? "))

# Ask user for number of rolls
num_rolls = int(input("How many times would you like to roll the dice? "))

# Roll the dice the specified number of times
rolls, total_sum = roll_dice(num_sides, num_rolls)

# Print out the individual rolls and their total sum
print("Individual rolls:", rolls)
print("Total sum of rolls:", total_sum)
print("Average roll: ", total_sum / num_rolls)
