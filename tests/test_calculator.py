# tests/test_calculator.py
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for the Calculator class."""

    @pytest.fixture(autouse=True)
    def setup(self):
        self.calc = Calculator()

    def test_add(self):
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-2, 3) == 1
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(1.5, 2.5) == 4.0
        assert self.calc.add(-1.5, -2.5) == -4.0

    def test_subtract(self):
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(-2, 3) == -5
        assert self.calc.subtract(0, 0) == 0
        assert self.calc.subtract(1.5, 0.5) == 1.0
        assert self.calc.subtract(-1.5, -0.5) == -1.0

    def test_multiply(self):
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(1.5, 2) == 3.0
        assert self.calc.multiply(-1.5, -2) == 3.0

    def test_divide(self):
        assert self.calc.divide(6, 3) == 2.0
        assert self.calc.divide(-6, 3) == -2.0
        assert self.calc.divide(1.5, 0.5) == 3.0
        assert self.calc.divide(-1.5, -0.5) == 3.0
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(1, 0)
