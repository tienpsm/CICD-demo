class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def add(self, a, b):
        """
        Add two numbers together.
        Args:
            a (int or float): First number
            b (int or float): Second number
        Returns:
            int or float: Sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract the second number from the first.
        Args:
            a (int or float): Number to subtract from
            b (int or float): Number to subtract
        Returns:
            int or float: Result of a - b
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.
        Args:
            a (int or float): First number
            b (int or float): Second number
        Returns:
            int or float: Product of a and b
        """
        return a * b

    def divide(self, a, b):
        """
        Divide the first number by the second.
        Args:
            a (int or float): Numerator
            b (int or float): Denominator
        Returns:
            float: Result of a / b
        Raises:
            ZeroDivisionError: If b is zero
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
