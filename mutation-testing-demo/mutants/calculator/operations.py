"""Operações matemáticas básicas."""

import math
from typing import Union

Number = Union[int, float]
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class Calculator:
    """Calculadora com operações básicas."""
    
    def xǁCalculatorǁadd__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Soma dois números."""
        return a + b
    
    def xǁCalculatorǁadd__mutmut_1(self, a: Number, b: Number) -> Number:
        """Soma dois números."""
        return a - b
    
    xǁCalculatorǁadd__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁadd__mutmut_1': xǁCalculatorǁadd__mutmut_1
    }
    
    def add(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁadd__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁadd__mutmut_mutants"), args, kwargs, self)
        return result 
    
    add.__signature__ = _mutmut_signature(xǁCalculatorǁadd__mutmut_orig)
    xǁCalculatorǁadd__mutmut_orig.__name__ = 'xǁCalculatorǁadd'
    
    def xǁCalculatorǁsubtract__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Subtrai dois números."""
        return a - b
    
    def xǁCalculatorǁsubtract__mutmut_1(self, a: Number, b: Number) -> Number:
        """Subtrai dois números."""
        return a + b
    
    xǁCalculatorǁsubtract__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁsubtract__mutmut_1': xǁCalculatorǁsubtract__mutmut_1
    }
    
    def subtract(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁsubtract__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁsubtract__mutmut_mutants"), args, kwargs, self)
        return result 
    
    subtract.__signature__ = _mutmut_signature(xǁCalculatorǁsubtract__mutmut_orig)
    xǁCalculatorǁsubtract__mutmut_orig.__name__ = 'xǁCalculatorǁsubtract'
    
    def xǁCalculatorǁmultiply__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Multiplica dois números."""
        return a * b
    
    def xǁCalculatorǁmultiply__mutmut_1(self, a: Number, b: Number) -> Number:
        """Multiplica dois números."""
        return a / b
    
    xǁCalculatorǁmultiply__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁmultiply__mutmut_1': xǁCalculatorǁmultiply__mutmut_1
    }
    
    def multiply(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁmultiply__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁmultiply__mutmut_mutants"), args, kwargs, self)
        return result 
    
    multiply.__signature__ = _mutmut_signature(xǁCalculatorǁmultiply__mutmut_orig)
    xǁCalculatorǁmultiply__mutmut_orig.__name__ = 'xǁCalculatorǁmultiply'
    
    def xǁCalculatorǁdivide__mutmut_orig(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_1(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b != 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_2(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 1:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_3(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError(None)
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_4(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("XXDivisão por zero não é permitidaXX")
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_5(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("divisão por zero não é permitida")
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_6(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("DIVISÃO POR ZERO NÃO É PERMITIDA")
        return a / b
    
    def xǁCalculatorǁdivide__mutmut_7(self, a: Number, b: Number) -> Number:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a * b
    
    xǁCalculatorǁdivide__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁdivide__mutmut_1': xǁCalculatorǁdivide__mutmut_1, 
        'xǁCalculatorǁdivide__mutmut_2': xǁCalculatorǁdivide__mutmut_2, 
        'xǁCalculatorǁdivide__mutmut_3': xǁCalculatorǁdivide__mutmut_3, 
        'xǁCalculatorǁdivide__mutmut_4': xǁCalculatorǁdivide__mutmut_4, 
        'xǁCalculatorǁdivide__mutmut_5': xǁCalculatorǁdivide__mutmut_5, 
        'xǁCalculatorǁdivide__mutmut_6': xǁCalculatorǁdivide__mutmut_6, 
        'xǁCalculatorǁdivide__mutmut_7': xǁCalculatorǁdivide__mutmut_7
    }
    
    def divide(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁdivide__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁdivide__mutmut_mutants"), args, kwargs, self)
        return result 
    
    divide.__signature__ = _mutmut_signature(xǁCalculatorǁdivide__mutmut_orig)
    xǁCalculatorǁdivide__mutmut_orig.__name__ = 'xǁCalculatorǁdivide'
    
    def xǁCalculatorǁpower__mutmut_orig(self, base: Number, exponent: Number) -> Number:
        """Calcula base elevado ao expoente."""
        return base ** exponent
    
    def xǁCalculatorǁpower__mutmut_1(self, base: Number, exponent: Number) -> Number:
        """Calcula base elevado ao expoente."""
        return base * exponent
    
    xǁCalculatorǁpower__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁpower__mutmut_1': xǁCalculatorǁpower__mutmut_1
    }
    
    def power(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁpower__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁpower__mutmut_mutants"), args, kwargs, self)
        return result 
    
    power.__signature__ = _mutmut_signature(xǁCalculatorǁpower__mutmut_orig)
    xǁCalculatorǁpower__mutmut_orig.__name__ = 'xǁCalculatorǁpower'
    
    def xǁCalculatorǁsquare_root__mutmut_orig(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_1(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number <= 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_2(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 1:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_3(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError(None)
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_4(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("XXRaiz quadrada de número negativo não é realXX")
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_5(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("raiz quadrada de número negativo não é real")
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_6(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("RAIZ QUADRADA DE NÚMERO NEGATIVO NÃO É REAL")
        return math.sqrt(number)
    
    def xǁCalculatorǁsquare_root__mutmut_7(self, number: Number) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return math.sqrt(None)
    
    xǁCalculatorǁsquare_root__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁsquare_root__mutmut_1': xǁCalculatorǁsquare_root__mutmut_1, 
        'xǁCalculatorǁsquare_root__mutmut_2': xǁCalculatorǁsquare_root__mutmut_2, 
        'xǁCalculatorǁsquare_root__mutmut_3': xǁCalculatorǁsquare_root__mutmut_3, 
        'xǁCalculatorǁsquare_root__mutmut_4': xǁCalculatorǁsquare_root__mutmut_4, 
        'xǁCalculatorǁsquare_root__mutmut_5': xǁCalculatorǁsquare_root__mutmut_5, 
        'xǁCalculatorǁsquare_root__mutmut_6': xǁCalculatorǁsquare_root__mutmut_6, 
        'xǁCalculatorǁsquare_root__mutmut_7': xǁCalculatorǁsquare_root__mutmut_7
    }
    
    def square_root(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁsquare_root__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁsquare_root__mutmut_mutants"), args, kwargs, self)
        return result 
    
    square_root.__signature__ = _mutmut_signature(xǁCalculatorǁsquare_root__mutmut_orig)
    xǁCalculatorǁsquare_root__mutmut_orig.__name__ = 'xǁCalculatorǁsquare_root'
    
    def xǁCalculatorǁis_even__mutmut_orig(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 == 0
    
    def xǁCalculatorǁis_even__mutmut_1(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number / 2 == 0
    
    def xǁCalculatorǁis_even__mutmut_2(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 3 == 0
    
    def xǁCalculatorǁis_even__mutmut_3(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 != 0
    
    def xǁCalculatorǁis_even__mutmut_4(self, number: int) -> bool:
        """Verifica se um número é par."""
        return number % 2 == 1
    
    xǁCalculatorǁis_even__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁis_even__mutmut_1': xǁCalculatorǁis_even__mutmut_1, 
        'xǁCalculatorǁis_even__mutmut_2': xǁCalculatorǁis_even__mutmut_2, 
        'xǁCalculatorǁis_even__mutmut_3': xǁCalculatorǁis_even__mutmut_3, 
        'xǁCalculatorǁis_even__mutmut_4': xǁCalculatorǁis_even__mutmut_4
    }
    
    def is_even(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁis_even__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁis_even__mutmut_mutants"), args, kwargs, self)
        return result 
    
    is_even.__signature__ = _mutmut_signature(xǁCalculatorǁis_even__mutmut_orig)
    xǁCalculatorǁis_even__mutmut_orig.__name__ = 'xǁCalculatorǁis_even'
    
    def xǁCalculatorǁfactorial__mutmut_orig(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_1(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n <= 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_2(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 1:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_3(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError(None)
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_4(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("XXFatorial não definido para números negativosXX")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_5(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_6(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("FATORIAL NÃO DEFINIDO PARA NÚMEROS NEGATIVOS")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_7(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n < 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_8(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 2:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_9(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 2
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_10(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = None
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_11(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 2
        for i in range(2, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_12(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(None, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_13(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, None):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_14(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_15(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, ):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_16(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(3, n + 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_17(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n - 1):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_18(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 2):
            result *= i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_19(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result = i
        return result
    
    def xǁCalculatorǁfactorial__mutmut_20(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Fatorial não definido para números negativos")
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result /= i
        return result
    
    xǁCalculatorǁfactorial__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCalculatorǁfactorial__mutmut_1': xǁCalculatorǁfactorial__mutmut_1, 
        'xǁCalculatorǁfactorial__mutmut_2': xǁCalculatorǁfactorial__mutmut_2, 
        'xǁCalculatorǁfactorial__mutmut_3': xǁCalculatorǁfactorial__mutmut_3, 
        'xǁCalculatorǁfactorial__mutmut_4': xǁCalculatorǁfactorial__mutmut_4, 
        'xǁCalculatorǁfactorial__mutmut_5': xǁCalculatorǁfactorial__mutmut_5, 
        'xǁCalculatorǁfactorial__mutmut_6': xǁCalculatorǁfactorial__mutmut_6, 
        'xǁCalculatorǁfactorial__mutmut_7': xǁCalculatorǁfactorial__mutmut_7, 
        'xǁCalculatorǁfactorial__mutmut_8': xǁCalculatorǁfactorial__mutmut_8, 
        'xǁCalculatorǁfactorial__mutmut_9': xǁCalculatorǁfactorial__mutmut_9, 
        'xǁCalculatorǁfactorial__mutmut_10': xǁCalculatorǁfactorial__mutmut_10, 
        'xǁCalculatorǁfactorial__mutmut_11': xǁCalculatorǁfactorial__mutmut_11, 
        'xǁCalculatorǁfactorial__mutmut_12': xǁCalculatorǁfactorial__mutmut_12, 
        'xǁCalculatorǁfactorial__mutmut_13': xǁCalculatorǁfactorial__mutmut_13, 
        'xǁCalculatorǁfactorial__mutmut_14': xǁCalculatorǁfactorial__mutmut_14, 
        'xǁCalculatorǁfactorial__mutmut_15': xǁCalculatorǁfactorial__mutmut_15, 
        'xǁCalculatorǁfactorial__mutmut_16': xǁCalculatorǁfactorial__mutmut_16, 
        'xǁCalculatorǁfactorial__mutmut_17': xǁCalculatorǁfactorial__mutmut_17, 
        'xǁCalculatorǁfactorial__mutmut_18': xǁCalculatorǁfactorial__mutmut_18, 
        'xǁCalculatorǁfactorial__mutmut_19': xǁCalculatorǁfactorial__mutmut_19, 
        'xǁCalculatorǁfactorial__mutmut_20': xǁCalculatorǁfactorial__mutmut_20
    }
    
    def factorial(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCalculatorǁfactorial__mutmut_orig"), object.__getattribute__(self, "xǁCalculatorǁfactorial__mutmut_mutants"), args, kwargs, self)
        return result 
    
    factorial.__signature__ = _mutmut_signature(xǁCalculatorǁfactorial__mutmut_orig)
    xǁCalculatorǁfactorial__mutmut_orig.__name__ = 'xǁCalculatorǁfactorial'
    