# This program calculates the chance to get the percentage with the Roll All button
#  more or equal than what you specify.
# This version of the program only calculates the rolls of one mod. 
#  It cannot calculate the rolls of several different mods at the same time.

import random
import statistics
import argparse
import math

def calculate_the_chance(number_of_slots, number_of_options, desired_percentage, number_of_trials=100000):
    success_roll_counter = 0
    for trial in range(number_of_trials):
        roll_sum = 0
        for slot in range(number_of_slots):
            mod_roll = random.uniform(0, number_of_options)
            if mod_roll < 1:
                percentage_roll = random.uniform(0, 100)
                if percentage_roll < 50:
                    roll_sum += 1
                    continue
                if percentage_roll < 80:
                    roll_sum += 2
                    continue
                if percentage_roll < 95:
                    roll_sum += 3
                    continue
                if percentage_roll < 99:
                    roll_sum += 4
                    continue
                roll_sum += 5
        if roll_sum >= desired_percentage:
            success_roll_counter += 1
    return success_roll_counter*1.0/number_of_trials


if __name__ == '__main__':
    # Number of slots that you've unlocked.
    # In Melvor Idle 1.0.1, there are three Standard and three Unique slots.
    # Therefore, the following variable is expected to have values 1, 2, or 3.
    number_of_slots = 3
    
    # Number of mod options in the slot
    # For instance, if a Standard slot can have 4 different mods in it, put 4 here.
    number_of_options = 4

    # The lower bound for the desired sum of bonuses that you want to get.
    # For instance, example, if you want at least 5% fishing reduction, you put 5 in there.
    desired_percentage = 10

    # Number of trials to get the final average from.
    number_of_trials = 100000

    example_text = '''examples:
    python melvor-astrology-roll-sum-chance.py
    python melvor-astrology-roll-sum-chance.py -s 2 -o 5 -p 4'''

    parser = argparse.ArgumentParser(epilog=example_text, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-s', '--number-of-slots', default=number_of_slots, type=int)
    parser.add_argument('-o', '--number-of-options', default=number_of_options, type=int)
    parser.add_argument('-p', '--desired-percentage', default=desired_percentage, type=int)
    parser.add_argument('-t', '--number-of-trials', default=number_of_trials, type=int)
    args = parser.parse_args()

    print ('\r\n Melvor Idle: Astrology Sum Chance calculator\r\n')
    print ('Starting the simulation with the parameters in the source file: \r\n')

    print ('Number of slots:', args.number_of_slots)
    print ('Number of options in a slot:', args.number_of_options)
    print ('Desired percentage:', args.desired_percentage)
    print ('Number of trials:', args.number_of_trials, '\r\n')

    success_chance = calculate_the_chance(args.number_of_slots, args.number_of_options, args.desired_percentage, args.number_of_trials)

    print('The success chance for one Roll All is', success_chance, '\r\n')
    if success_chance == 0 or success_chance == 1:
        exit()
    print('For 50% chance to roll', args.desired_percentage, '% total, you need to roll', math.ceil(math.log(0.5, 1-success_chance)), 'times.')
    print('For 75% chance to roll', args.desired_percentage, '% total, you need to roll', math.ceil(math.log(1 - 0.75, 1-success_chance)), 'times.')
    print('For 95% chance to roll', args.desired_percentage, '% total, you need to roll', math.ceil(math.log(1 - 0.95, 1-success_chance)), 'times.')
    
