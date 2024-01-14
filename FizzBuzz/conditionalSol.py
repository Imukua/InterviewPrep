#!/usr/bin/python3
"""
FizzBuzz solution by utilising conditionals
"""


def FizzBuzz(num: int) -> str:
    """
    Args: 
        num: int: number to analyse
    Return:
        'Fizz' if num divisible by three
        'Buzz' if nuum divisiblle by five
        'FizzBuzz' if num divisible by both 3 & 5
    """

    if num % 3 == 0:
        if num % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return None

if __name__ == "__main__":
    num = input("Enter number: ")
    try:
        num = int(num)
        print(FizzBuzz(int(num)))
    except ValueError:
        print("Input number only!")
    