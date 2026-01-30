import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import random
import sys

# Import the function to test
from specifikacija1_kods import spele


class TestSpele(unittest.TestCase):
    """Test cases for the number guessing game (spele function)"""

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_guess_first_try(self, mock_stdout, mock_input, mock_randint):
        """Test when the user guesses correctly on the first try"""
        mock_randint.return_value = 50
        mock_input.side_effect = ['50', 'nē']  # Correct guess, don't play again
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Apsveicam!", output)
        self.assertIn("50", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_too_high(self, mock_stdout, mock_input, mock_randint):
        """Test when user guesses a number higher than the target"""
        mock_randint.return_value = 30
        mock_input.side_effect = ['60', '30', 'nē']  # Guess too high, then correct
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Mans skaitlis ir mazāks!", output)
        self.assertIn("Apsveicam!", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_too_low(self, mock_stdout, mock_input, mock_randint):
        """Test when user guesses a number lower than the target"""
        mock_randint.return_value = 70
        mock_input.side_effect = ['40', '70', 'nē']  # Guess too low, then correct
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Mans skaitlis ir lielāks!", output)
        self.assertIn("Apsveicam!", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_lose_game_all_attempts_used(self, mock_stdout, mock_input, mock_randint):
        """Test when user loses by using all 10 attempts without guessing correctly"""
        mock_randint.return_value = 50
        # Make 10 wrong guesses
        mock_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Jūs zaudējāt", output)
        self.assertIn("50", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_attempts_before_correct(self, mock_stdout, mock_input, mock_randint):
        """Test with multiple wrong attempts before the correct guess"""
        mock_randint.return_value = 50
        mock_input.side_effect = ['25', '75', '50', 'nē']  # Wrong, wrong, correct
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Mans skaitlis ir lielāks!", output)  # 25 is too low
        self.assertIn("Mans skaitlis ir mazāks!", output)   # 75 is too high
        self.assertIn("Apsveicam!", output)  # Finally correct

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_remaining_attempts_counter(self, mock_stdout, mock_input, mock_randint):
        """Test that the remaining attempts counter decreases"""
        mock_randint.return_value = 50
        mock_input.side_effect = ['25', '75', '50', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Atlikušie mēģinājumi: 10", output)  # First attempt
        self.assertIn("Atlikušie mēģinājumi: 9", output)   # Second attempt
        self.assertIn("Atlikušie mēģinājumi: 8", output)   # Third attempt

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_again_yes_response(self, mock_stdout, mock_input, mock_randint):
        """Test that the game asks if user wants to play again"""
        mock_randint.side_effect = [50, 75]  # Two different numbers for two games
        mock_input.side_effect = ['50', 'jā', '75', 'nē']  # Play game, answer jā, play again, answer nē
        
        spele()
        
        output = mock_stdout.getvalue()
        # Should call input twice for play again prompts (once per game)
        self.assertEqual(mock_input.call_count, 4)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_number_range(self, mock_stdout, mock_input, mock_randint):
        """Test that the game uses numbers in range 1-100"""
        mock_randint.return_value = 50
        mock_input.side_effect = ['50', 'nē']
        
        spele()
        
        # Verify random.randint was called with correct parameters
        mock_randint.assert_called_with(1, 100)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_exact_match_on_last_attempt(self, mock_stdout, mock_input, mock_randint):
        """Test winning on the 10th (last) attempt"""
        mock_randint.return_value = 50
        # 9 wrong guesses, then correct on 10th
        mock_input.side_effect = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '50', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Apsveicam!", output)
        self.assertNotIn("Jūs zaudējāt", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_boundary_value_1(self, mock_stdout, mock_input, mock_randint):
        """Test guessing the minimum boundary value (1)"""
        mock_randint.return_value = 1
        mock_input.side_effect = ['1', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Apsveicam!", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_boundary_value_100(self, mock_stdout, mock_input, mock_randint):
        """Test guessing the maximum boundary value (100)"""
        mock_randint.return_value = 100
        mock_input.side_effect = ['100', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Apsveicam!", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_play_again_case_insensitive(self, mock_stdout, mock_input, mock_randint):
        """Test that 'jā' response works regardless of case"""
        mock_randint.side_effect = [50, 75]
        # Test with different cases (Jā, JĀ)
        mock_input.side_effect = ['50', 'Jā', '75', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        # Should start second game without issue
        self.assertIn("Esmu iedomājies nejaušu skaitli", output)


class TestGameIntegration(unittest.TestCase):
    """Integration tests for the number guessing game"""

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_binary_search_strategy(self, mock_stdout, mock_input, mock_randint):
        """Test using a binary search strategy to guess the number"""
        mock_randint.return_value = 50
        # Binary search: 50 (middle), should be exact match
        mock_input.side_effect = ['50', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Apsveicam!", output)

    @patch('random.randint')
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_sequential_guessing(self, mock_stdout, mock_input, mock_randint):
        """Test guessing sequentially from 1 upward"""
        mock_randint.return_value = 5
        mock_input.side_effect = ['1', '2', '3', '4', '5', 'nē']
        
        spele()
        
        output = mock_stdout.getvalue()
        self.assertIn("Apsveicam!", output)
        # Check for the hints about lower/higher
        self.assertIn("Mans skaitlis ir lielāks!", output)


if __name__ == '__main__':
    unittest.main()
