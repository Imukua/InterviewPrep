#!/usr/bin/python3
"""
FizzBuzz using lambda and map functions
"""


print(
    *map(
        lambda a: "Fizz" * (a % 3 == 0) + "Buzz" * (a % 5 == 0)
        or str(a) + ": No Fizz No Buzz",
        range(1, 100),
    ),
    sep="\n"
)
