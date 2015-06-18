# Copyright (c) 2012 by Ken Hagler <khagler@orange-road.com>.
"""
The diceware module reads a Diceware wordlist from a file and returns a
dictionary of words with the five digit roll (from 111111 to 666666) as
the key.
"""

import argparse
import csv


def read_wordlist(wordlist_file):
    """
    Read a wordlist file and return a dictionary containing that wordlist.

    @param wordlist_file: The wordlist file to read.
    @type wordlist_file: string
    """
    wordlist_dict = {}
    with open(wordlist_file, 'rb') as wordlist:
        wordreader = csv.reader(wordlist, delimiter='\t',
                                quoting=csv.QUOTE_NONE)
        for row in wordreader:
            wordlist_dict[row[0]] = row[1]
    return wordlist_dict


def validate_roll(roll):
    """
    Check to see whether a roll is valid.

    A valid roll is a string containing five numbers from one to six.

    @param roll: The roll to validate
    @type roll: string

    @return: True if the roll is valid, False if it's not.
    @rtype: boolean
    """
    # Make sure we only have numbers first.
    if not roll.isdigit():
        print("Diceware rolls must be numbers.")
        return False
    # Make sure the roll has exactly five digits.
    if len(roll) != 5:
        print("Diceware rolls must be exactly five digits.")
        return False
    # Now loop through each digit making sure it's in the allowed range
    # of 1 through 6.
    for digit in roll:
        if not 1 <= int(digit) <= 6:
            print("Diceware uses six-sided dice. "
                  "Only numbers from 1 through 6 are valid.")
            return False
    # If we got here without returning False, it's valid.
    return True


def get_rolls(words):
    """
    Prompt for a series of rolls, and return a list of the rolls.

    @param words: The number of rolls to prompt for.
    @type words: integer

    @return: A list of rolls.
    @rtype: list
    """
    roll_list = []
    # Once through the loop for each word. The words parameter should be an
    # integer, but convert it to be safe. Since the number of the current word
    # will be seen by the user, we want to start from 1, not 0.
    for num in range(1, int(words) + 1):
        while True:
            roll = raw_input("Please enter the rolls for word {}:".format(num))
            if validate_roll(roll):
                break
        roll_list.append(roll)
    return roll_list

def get_passphrase(rolls, wordlist):
    """
    Return a passphrase for a list of rolls.

    @param rolls: A list of rolls entered by the user.
    @type rolls: list

    @param wordlist: A dictionary from which the passphrase will be looked up.
    @type wordlist: dict

    @return: A passphrase.
    @rtype: string
    """
    passphrase = ""
    # Loop through the list of rolls, looking each up in the wordlist and
    # adding the corresponding word to the passphrase.
    for roll in rolls:
        passphrase += wordlist[roll] + " "
    return passphrase.strip()

def generate_passphrase(words, wordlist_file):
    # Start by reading in the wordlist.
    wordlist= read_wordlist(wordlist_file)
    # Next get the list of rolls
    rolls = get_rolls(words)
    # Finally, get the passphrase.
    return get_passphrase(rolls, wordlist)

if __name__ == "__main__":
    # Set up the parser and parse the arguements
    parser = argparse.ArgumentParser(
        description="Diceware Passphrase Generator")
    parser.add_argument("words", help="number of words in the passphrase",
                        type=int)
    parser.add_argument("-w", "--wordlist",
                        default="wordlists/defaultwordlist.txt",
                        help="path to a Diceware wordlist file")
    args = parser.parse_args()

    # Generate the passphrase
    print(generate_passphrase(args.words, args.wordlist))
