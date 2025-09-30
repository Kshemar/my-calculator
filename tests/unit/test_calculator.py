"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, div, divide, mul, multiply, subtract

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class

class TestMultiplyDivide:

    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50

    def test_multiply_negative_numbers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5
        assert divide(-9, -3) == 3

    def test_add_negative_numbers(self):
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2
    def test_subtract_negative_numbers(self):
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2
    def test_mul_positive_numbers(self):
        """Test multiplication of positive numbers"""
        assert mul(2, 3) == 6
        assert mul(5, 4) == 20
    def test_div_positive_numbers(self):
        """Test division of positive numbers"""
        assert div(6, 3) == 2
        assert div(10, 2) == 5
    