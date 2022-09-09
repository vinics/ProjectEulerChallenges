'''
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

link: https://projecteuler.net/problem=5
'''

from math import factorial


def main():
    # Input params
    minRangeNumber = 1
    maxRangeNumber = 20

    target = range(minRangeNumber, maxRangeNumber + 1)
    factorEncounterScore = 0
    
    for number in range(maxRangeNumber, factorial(maxRangeNumber) + 1, maxRangeNumber):
        for factor in target:
            # Check if it is divisible
            if number % factor != 0:
                break
            factorEncounterScore += 1

        if factorEncounterScore == len(target):
            print(f"RESULT: {number}")
            break

        factorEncounterScore = 0                


if __name__ == "__main__":
    main()