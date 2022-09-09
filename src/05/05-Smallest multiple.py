'''
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

link: https://projecteuler.net/problem=5
'''

from math import factorial


def main():
    minRangeNumber = 1
    maxRangeNumber = 20

    target = range(minRangeNumber, maxRangeNumber)
    factorEncounterScore = 0
    
    for number in range(maxRangeNumber, factorial(maxRangeNumber), maxRangeNumber):
        for factor in target:
            # Check if it is divisible
            if number % factor != 0:
                break
            factorEncounterScore += 1

        if factorEncounterScore == len(target):
            print(f"RESULT: {number}")
            break

        factorEncounterScore = 0                

    
    




#     number = 20

#     while not isDivisible(range(1, 21), number):
#         print(f"# {number}: Not valid")
#         number += 1

#     print(f"Smallest positive number that is evenly divisible by all of the numbers from 1 to 20")
#     print(f"Result: {number}")

# def isDivisible(range: range, value: int) -> bool:
#     for num in range:
#         if value % num != 0:
#             print(f"\t - {value} Not divible by {num}")
#             return False
#     return True

if __name__ == "__main__":
    main()