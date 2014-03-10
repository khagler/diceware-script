from unittest import TestCase
from mock import MagicMock, patch
import diceware

class TestDiceware(TestCase):
    def test_read_wordlist(self):
        test_words = {'11111': 'a', '12345': 'apathy', '66666': '@'}
        # Test that the wordlist is read successfully.
        self.assertDictContainsSubset(test_words, diceware.read_wordlist())

    def test_validate_roll(self):
        # Test with a valid roll.
        self.assertTrue(diceware.validate_roll("11111"))
        # Test with a non-numeric value in the roll.
        self.assertFalse(diceware.validate_roll("A11111"))
        # Test with a roll out of the allowed range.
        self.assertFalse(diceware.validate_roll("11117"))
        # Test with a roll that is the wrong length.
        self.assertFalse(diceware.validate_roll("111111"))

    @patch('__builtin__.raw_input')
    def test_get_rolls(self, mock_raw_input):
        mock_raw_input.side_effect = ['11111', '22222', '33333', '44444',
                                      '55555', '66666', '77777']
        # Test that a wordlist is returned.
        self.assertEqual(diceware.get_rolls(5),
                         ['11111', '22222', '33333', '44444', '55555'])
        # Test with a string for the number of words.
        self.assertEqual(diceware.get_rolls('1'), ['66666'])
