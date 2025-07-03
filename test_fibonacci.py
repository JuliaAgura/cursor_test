import unittest
from main import fibonacci_sequence


class TestFibonacciSequence(unittest.TestCase):
    """Test cases for the fibonacci_sequence function."""

    def test_fibonacci_zero_numbers(self):
        """Test that requesting 0 numbers returns empty list."""
        result = fibonacci_sequence(0)
        # Edge case: no numbers requested should return empty list
        self.assertEqual(result, [])

    def test_fibonacci_negative_numbers(self):
        """Test that requesting negative numbers returns empty list."""
        # Test with -1 (just below zero)
        result = fibonacci_sequence(-1)
        self.assertEqual(result, [])
        
        # Test with a more negative number to ensure robustness
        result = fibonacci_sequence(-5)
        self.assertEqual(result, [])

    def test_fibonacci_one_number(self):
        """Test that requesting 1 number returns [0]."""
        result = fibonacci_sequence(1)
        # First fibonacci number is always 0
        self.assertEqual(result, [0])

    def test_fibonacci_two_numbers(self):
        """Test that requesting 2 numbers returns [0, 1]."""
        result = fibonacci_sequence(2)
        # First two fibonacci numbers are 0 and 1
        self.assertEqual(result, [0, 1])

    def test_fibonacci_small_sequences(self):
        """Test small fibonacci sequences."""
        # Test 3 numbers: 0, 1, 1 (third number is 0+1=1)
        self.assertEqual(fibonacci_sequence(3), [0, 1, 1])
        
        # Test 4 numbers: 0, 1, 1, 2 (fourth number is 1+1=2)
        self.assertEqual(fibonacci_sequence(4), [0, 1, 1, 2])
        
        # Test 5 numbers: 0, 1, 1, 2, 3 (fifth number is 1+2=3)
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])

    def test_fibonacci_medium_sequence(self):
        """Test a medium-sized fibonacci sequence."""
        # Expected sequence for first 10 fibonacci numbers
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        result = fibonacci_sequence(10)
        self.assertEqual(result, expected)

    def test_fibonacci_longer_sequence(self):
        """Test a longer fibonacci sequence."""
        # Expected sequence for first 15 fibonacci numbers
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        result = fibonacci_sequence(15)
        self.assertEqual(result, expected)

    def test_fibonacci_sequence_properties(self):
        """Test mathematical properties of fibonacci sequence."""
        sequence = fibonacci_sequence(10)
        
        # Verify the fundamental fibonacci property: F(n) = F(n-1) + F(n-2)
        # Start from index 2 since we need at least 2 previous numbers
        for i in range(2, len(sequence)):
            # Each number should equal the sum of the two preceding numbers
            self.assertEqual(sequence[i], sequence[i-1] + sequence[i-2])

    def test_fibonacci_sequence_length(self):
        """Test that the returned sequence has the correct length."""
        # Test various sequence lengths to ensure function returns correct count
        for n in [1, 5, 10, 15, 20]:
            result = fibonacci_sequence(n)
            # Length of returned list should match requested count
            self.assertEqual(len(result), n)

    def test_fibonacci_sequence_types(self):
        """Test that the function returns the correct types."""
        result = fibonacci_sequence(5)
        
        # Ensure the function returns a list
        self.assertIsInstance(result, list)
        
        # Ensure all elements in the list are integers
        self.assertTrue(all(isinstance(num, int) for num in result))

    def test_fibonacci_first_elements(self):
        """Test that the first elements are always correct."""
        # Test multiple sequence lengths to ensure first elements are consistent
        for n in range(1, 20):
            result = fibonacci_sequence(n)
            
            # First element should always be 0 (F(0) = 0)
            self.assertEqual(result[0], 0)
            
            # If sequence has more than 1 element, second should be 1 (F(1) = 1)
            if n > 1:
                self.assertEqual(result[1], 1)


if __name__ == "__main__":
    # Run all tests when script is executed directly
    unittest.main() 