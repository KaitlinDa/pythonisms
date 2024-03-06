from decorators.logging_decorator import logging_decorator
from decorators.timing_decorator import timing_decorator

@timing_decorator
@logging_decorator
def sample_function(n):
    """Function that calculates the sum of numbers from 1 to n"""
    total = sum(range(1, n+1))
    return total

print(sample_function(5))
