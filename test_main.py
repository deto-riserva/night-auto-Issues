"""Unit tests for calculator functions."""

import unittest
from main import add, subtract, multiply


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test add function."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(10, -7), 3)
    
    def test_subtract(self):
        """Test subtract function."""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(-5, -3), -2)
        self.assertEqual(subtract(10, -7), 17)
    
    def test_multiply(self):
        """Test multiply function."""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-4, -5), 20)
        self.assertEqual(multiply(1, 100), 100)


if __name__ == "__main__":
    unittest.main()
