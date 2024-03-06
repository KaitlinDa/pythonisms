# Lab 42 - Class 401d24

## Project
Pythonisms

## Author

Kaitlin Davis | March 2024

## About
The "Pythonisms" project is a demonstration of Python's unique features and idioms, aiming to showcase how Python's specific characteristics can simplify programming tasks and enhance code readability and efficiency. This project covers iterators, generators, decorators, and dunder methods, providing practical examples of their usage and benefits.

## Features
- **Iterators/Generators**: Custom collection implemented to be iterable, usable in for-loops and list comprehensions, and easily convertible to list or other collection types.
- **Decorators**: 
  - `logging_decorator`: Adds logging functionality to any function, logging its execution and return values.
  - `timing_decorator`: Measures and prints the execution time of the decorated function.
- **Dunder Methods**: Custom data structure implementation showcasing the use of dunder methods for equality checks, truthiness evaluation, and more, enhancing the Pythonic feel of the code.

## User Acceptance Tests
The project includes unit tests that demonstrate the functionality of the implemented features:
- Tests for iterator/generator ensuring correct iteration behavior.
- Tests for decorators verifying their added behaviors (logging and timing) without affecting the original function's output.
- Tests for dunder methods ensuring correct behavior of custom equality checks and truthiness evaluations.

To run the tests, ensure you have `pytest` installed, and execute the following command in the project root directory:
```bash
pytest
