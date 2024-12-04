# tests/test_calculator.py
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for the Calculator class."""

    def setup_method(self):
        """
        Setup method to create a new Calculator instance
        before each test method.
        """
        self.calc = Calculator()

    def test_add(self):
        """Test the add method with various inputs."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(1.5, 2.5) == 4.0

    def test_subtract(self):
        """Test the subtract method with various inputs."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(-1, 1) == -2
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.subtract(5.5, 2.5) == 3.0

    def test_multiply(self):
        """Test the multiply method with various inputs."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(1.5, 2) == 3.0

    def test_divide(self):
        """Test the divide method with various inputs."""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(-6, 2) == -3
        assert self.calc.divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        """
        Test that dividing by zero raises a ZeroDivisionError.
        Uses pytest.raises to check for the specific exception.
        """
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            self.calc.divide(5, 0)
