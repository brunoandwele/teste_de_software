"""Operações matemáticas básicas."""

import math
from typing import Union

Number = Union[int, float]


class Calculator:
    """Calculadora com operações básicas."""
    
    def add(self, a: Number, b: Number) -> Number:
        """Soma dois números."""
        return a + b
    
    def subtract(self, a: Number, b: Number) -> Number:
        """Subtrai dois números."""
        return a - b
    
    def multiply(self, a: Number, b: Number) -> Number:
        """Multiplica dois números."""
        return a * b
    
    def divide(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    def power(self, base: Number, exponent: Number) -> Number:
        """Calcula base elevado ao expoente."""
        return base ** exponent
    
    def square_root(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)
    
    def is_even(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 == 0
    
    def factorial(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    