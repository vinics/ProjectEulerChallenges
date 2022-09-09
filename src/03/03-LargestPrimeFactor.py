'''
Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

link: https://projecteuler.net/problem=3
'''

# Stores in memory all calculated prime numbers
primeList = [2]
primeFactorList = []
factorMatchFlag = False

def main():
    number = int(input("Number: "))

    # In case the input is prime
    if isPrime(number):
        print(f"Largest prime factor: {number}")

    while not isPrime(number):
        factorMatchFlag = False

        for cursor in range(0, len(primeList)):
            if number % primeList[cursor] == 0:
                factorMatchFlag = True
                number = number // primeList[cursor]

                if primeList[cursor] not in primeFactorList:
                    primeFactorList.append(primeList[cursor])
        
        if factorMatchFlag == False:
            newPrime = primeList[-1] + 1

            while not isPrime(newPrime):
                newPrime += 1
            
            primeList.append(newPrime)

    if number not in primeFactorList and number != 1:
        primeFactorList.append(number)

    print(f"Largest prime factor: {max(primeFactorList)}")

def isPrime(num: int) -> bool:
    # Check if is already on the list
    if num in primeList:
        return True

    # Check if not positive
    if num <= 0:
        print(f"ERROR: Function's [isPrime] argument num must be a positive integer: Received({num})")
        exit(2)

    # Check if the i on the prime list
    if num in primeList:
        return True
    
    # Test the number
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    
    primeList.append(num)
    return True

if __name__ == "__main__":
    main()