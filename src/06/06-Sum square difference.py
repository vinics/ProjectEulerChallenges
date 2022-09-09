'''
Sum square difference

Problem 6

The sum of the squares of the first ten natural numbers is,

    1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


link: https://projecteuler.net/problem=6
'''
import sys

def main():
    # Input params
    limit = 100

    # App variable
    sumOfSquares = 0
    squareOfTheSum = 0

    for num in range(limit + 1):
        sumOfSquares += pow(num, 2)
        squareOfTheSum += num

    result = (pow(squareOfTheSum, 2) - sumOfSquares)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()