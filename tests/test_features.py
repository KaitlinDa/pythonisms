import logging
import pytest
from unittest import mock
from decorators.logging_decorator import logging_decorator
from decorators.timing_decorator import timing_decorator

def example_func(x):
    return x * x

def test_timing_decorator():
    decorated_func = timing_decorator(example_func)
    
    with mock.patch("time.perf_counter", side_effect=[0, 1]):
        assert decorated_func(5) == 25, "Timing decorator changed the output of the function."

def test_logging_decorator(caplog):
    decorated_func = logging_decorator(example_func)

    with caplog.at_level(logging.INFO):
        result = decorated_func(2)

    assert result == 4, "Logging decorator changed the output of the function."
    assert "Running 'example_func' with arguments (2,)" in caplog.text
    assert "'example_func' returned 4" in caplog.text

def test_decorators_preserve_metadata():
    decorated_func = logging_decorator(timing_decorator(example_func))
    
    assert decorated_func.__name__ == "example_func", "Decorator did not preserve function name."
    assert decorated_func.__doc__ == example_func.__doc__, "Decorator did not preserve docstring."

