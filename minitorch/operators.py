"""
Collection of the core mathematical operators used throughout the code base.
"""

import math
from typing import Callable, Iterable

# ## Task 0.1
#
# Implementation of a prelude of elementary functions.


def mul(x: float, y: float) -> float:
    return x * y


def id(x: float) -> float:
    return x


def add(x: float, y: float) -> float:
    return x + y


def neg(x: float) -> float:
    return -x


def lt(x: float, y: float) -> float:
    return 1 if x < y else 0


def eq(x: float, y: float) -> float:
    return 1 if x == y else 0


def max(x: float, y: float) -> float:
    return x if x >= y else y


def is_close(x: float, y: float) -> float:
    return 1 if abs(x - y) < 1e-2 else 0


def sigmoid(x: float) -> float:
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    return math.exp(x) / (1 + math.exp(x))


def relu(x: float) -> float:
    return x if x > 0 else 0


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def log_back(x: float, y: float) -> float:
    return y / x


def inv(x: float) -> float:
    return 1 / x


def inv_back(x: float, y: float) -> float:
    return -y / x**2


def relu_back(x: float, y: float) -> float:
    return y if x > 0 else 0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


def map(f: Callable) -> Callable:
    return lambda l: [f(x) for x in l]


def zipWith(f: Callable) -> Callable:
    return lambda l1, l2: [f(x, y) for x, y in zip(l1, l2)]


def reduce(f: Callable, start: float) -> Callable:
    def f2(l: Iterable) -> float:
        result = start
        for x in l:
            result = f(result, x)
        return result

    return f2


def negList(l: Iterable) -> Iterable:
    return map(neg)(l)


def addLists(l1: Iterable, l2: Iterable) -> Iterable:
    return zipWith(add)(l1, l2)


def sum(l: Iterable) -> float:
    return reduce(add, 0)(l)


def prod(l: Iterable) -> float:
    return reduce(mul, 1)(l)
