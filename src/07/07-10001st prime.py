'''
10001st prime

Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


link: https://projecteuler.net/problem=7
'''
import sys
import time

def main():
  getNthPrime(10001)

def getNthPrime(position):
  start_time = time.time()

  # Input params
  primePositions = position

  # App variables
  primeList = [2]
  currentValue = primeList[-1] + 1

  while len(primeList) < primePositions:
    isPrime = True

    for prime in primeList:
      if currentValue % prime == 0:
        isPrime = False
        currentValue += 1
        break
    
    if isPrime:
      primeList.append(currentValue)
      currentValue = primeList[-1] + 1
    

  print(f"Result: {primeList[-1]}")
  print(f" --- {time.time() - start_time}s seconds ---")




if __name__ == "__main__":
    main()