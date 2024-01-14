#!/usr/bin/python3
"""FizzBuzz concatenation solution"""


def FizzBuzz(num: int) -> str:
    """
    Args: 
        num: int: number to analyse
    Return:
        'Fizz' if num divisible by three
        'Buzz' if nuum divisiblle by five
        'FizzBuzz' if num divisible by both 3 & 5
    """
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + "No Fizz No Buzz"

    return string


if __name__ == "__main__":
    num = input("Enter number: ")
    try:
        num = int(num)
        print(FizzBuzz(int(num)))
    except ValueError:
        print("Input number only!")
