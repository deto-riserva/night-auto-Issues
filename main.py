"""Fibonacci sequence implementation."""


def fibonacci(n):
    """
    Return the nth Fibonacci number.
    
    The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    where each number is the sum of the two preceding ones.
    
    Args:
        n: The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
