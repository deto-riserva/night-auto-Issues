"""Unit tests for Fibonacci function."""

import unittest
from main import fibonacci


class TestFibonacci(unittest.TestCase):
    """Test cases for fibonacci function."""
    
    def test_fibonacci_base_cases(self):
        """Test fibonacci base cases."""
        self.assertEqual(fibonacci(0), 0, "fibonacci(0) should return 0")
        self.assertEqual(fibonacci(1), 1, "fibonacci(1) should return 1")
    
    def test_fibonacci_sequence(self):
        """Test fibonacci sequence values."""
        # Test the well-known Fibonacci sequence
        expected_values = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
            (6, 8),
            (7, 13),
            (8, 21),
            (9, 34),
            (10, 55),
        ]
        
        for n, expected in expected_values:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)
    
    def test_fibonacci_large_numbers(self):
        """Test fibonacci with larger indices."""
        self.assertEqual(fibonacci(15), 610)
        self.assertEqual(fibonacci(20), 6765)
    
    def test_fibonacci_invalid_input(self):
        """Test fibonacci with invalid input."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)


if __name__ == "__main__":
    unittest.main()
