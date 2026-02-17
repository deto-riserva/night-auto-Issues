"""Unit tests for Fibonacci module."""

import pytest
from fibonacci import fibonacci


class TestFibonacci:
    """Test cases for Fibonacci function."""

    def test_fibonacci_base_cases(self):
        """Test base cases (0 and 1)."""
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_sequence(self):
        """Test the Fibonacci sequence."""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, expected_val in enumerate(expected):
            assert fibonacci(i) == expected_val

    def test_fibonacci_large_number(self):
        """Test with a larger Fibonacci index."""
        assert fibonacci(10) == 55
        assert fibonacci(15) == 610

    def test_fibonacci_negative_number(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError):
            fibonacci(-1)
        with pytest.raises(ValueError):
            fibonacci(-10)
