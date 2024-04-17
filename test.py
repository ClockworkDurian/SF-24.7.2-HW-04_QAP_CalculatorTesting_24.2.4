import pytest
from app.calculator import Calculator
class TestCalculator:
    def setup(self):
        self.calculator = Calculator
    def test_multiply_success(self):
        assert self.calculator.multiply(self,3,5) == 15
    def test_division_success(self):
        assert self.calculator.division(self,15,3) == 5
    def test_subtraction_success(self):
        assert self.calculator.subtraction(self,3,5) == -2
    def test_adding_success(self):
        assert self.calculator.adding(self,3,5) == 8
    def teardown(self):
        print("Выполнение метода Teardown")