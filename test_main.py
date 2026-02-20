"""Unit tests for main module."""

import unittest
from main import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for hello_world function."""
    
    def test_hello_world(self):
        """Test hello_world returns correct string."""
        self.assertEqual(hello_world(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
