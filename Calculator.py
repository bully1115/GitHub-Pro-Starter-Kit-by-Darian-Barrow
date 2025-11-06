#!/usr/bin/env python3
"""
A simple calculator module with basic arithmetic operations.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Difference of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide first number by second number.
    
    Args:
        a (float): First number (numerator)
        b (float): Second number (denominator)
    
    Returns:
        float: Quotient of a divided by b
    
    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If attempting to divide by zero
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    try:
        # Test basic operations
        print("Basic Operations Test:")
        print("Add 2 + 3 =", add(2, 3))
        print("Subtract 5 - 1 =", subtract(5, 1))
        print("Multiply 4 * 3 =", multiply(4, 3))
        print("Divide 10 / 2 =", divide(10, 2))
        
        # Test error handling
        print("\nError Handling Test:")
        print("Trying to add string and number...")
        add("2", 3)  # Should raise TypeError
    except TypeError as e:
        print(f"TypeError caught: {e}")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
