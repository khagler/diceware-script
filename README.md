diceware-script
===============

Python script to assist with Diceware passphrase generation. It reads a Diceware wordlist from a file and returns a dictionary of words with the five digit roll (from 111111 to 666666) as the key.

Usage
-----
	python diceware.py <words in passphrase> [--wordlist /path/to/wordlist.txt]
Example:

	python diceware.py 5
Generate a passphrase give words long.

	python diceware.py 3 --wordlist foo.txt
Generate a three word passphrase using a wordlist contained in the `foo.txt` file.