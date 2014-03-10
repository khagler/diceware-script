# Copyright (c) 2012 by Ken Hagler <khagler@orange-road.com>.
"""
The diceware module reads a Diceware wordlist from a file and returns a
dictionary of words with the five digit roll (from 111111 to 666666) as
the key.
"""

import csv


def read_wordlist(wordlist_file="wordlists/defaultwordlist.txt"):
    """
    Read a wordlist file and return a dictionary containing that wordlist.

    @param wordlist: The wordlist file to read. Optional, defaults to the
        standard wordlist.
    @type wordlist: string
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
    # integer, but convert it to be safe.
    for num in range(int(words)):
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
