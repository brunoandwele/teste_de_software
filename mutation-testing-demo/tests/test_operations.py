"""Testes para as operações da calculadora."""

import pytest
import math
from calculator import Calculator


class TestCalculator:
    """Testes para a classe Calculator."""
    
    def setup_method(self):
        """Configuração executada antes de cada teste."""
        self.calc = Calculator()
    
    def test_add(self):
        """Testa a operação de soma."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
        assert self.calc.add(2.5, 1.5) == 4.0
    
    def test_subtract(self):
        """Testa a operação de subtração."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(-1, -1) == 0
        assert self.calc.subtract(10, 15) == -5
    
    def test_multiply(self):
        """Testa a operação de multiplicação."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(2.5, 4) == 10.0
    
    def test_divide(self):
        """Testa a operação de divisão."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(7, 2) == 3.5
        assert self.calc.divide(-6, 2) == -3
        
        # Teste de divisão por zero
        with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Testa a operação de potenciação."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(2, -1) == 0.5
        assert self.calc.power(9, 0.5) == 3.0
    
    def test_square_root(self):
        """Testa a operação de raiz quadrada."""
        assert self.calc.square_root(4) == 2.0
        assert self.calc.square_root(9) == 3.0
        assert self.calc.square_root(0) == 0.0
        assert abs(self.calc.square_root(2) - 1.4142135623730951) < 1e-10
        
        # Teste de raiz de número negativo
        with pytest.raises(ValueError, match="Raiz quadrada de número negativo não é real"):
            self.calc.square_root(-1)
    
    def test_is_even(self):
        """Testa a verificação de números pares."""
        assert self.calc.is_even(2) is True
        assert self.calc.is_even(3) is False
        assert self.calc.is_even(0) is True
        assert self.calc.is_even(-2) is True
        assert self.calc.is_even(-3) is False
    
    def test_factorial(self):
        """Testa o cálculo de fatorial."""
        assert self.calc.factorial(0) == 1
        assert self.calc.factorial(1) == 1
        assert self.calc.factorial(3) == 6
        assert self.calc.factorial(5) == 120
        
        # Teste de fatorial de número negativo
        with pytest.raises(ValueError, match="Fatorial não definido para números negativos"):
            self.calc.factorial(-1)
        