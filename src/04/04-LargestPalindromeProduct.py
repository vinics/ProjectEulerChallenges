'''
Largest palindrome product

Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

link: https://projecteuler.net/problem=4
'''

def main():
    largestNumber = 999
    
    pair = []
    largestPalindrome = 0
    
    for number1 in reversed(range(1, largestNumber + 1)):
        for number2 in reversed(range(1, largestNumber + 1)):
            product = number1 * number2

            if product == numberReverse(product):
                if largestPalindrome < product:
                    largestPalindrome = product
                    pair = [number1, number2]
    
    print(f"The largest palindromic number from two 3-digit numbers is {largestPalindrome}")
    print(f"from {pair[0]} x {pair[1]}")


def numberReverse(number):
    digits = list(map(int, str(number)))
    digits.reverse()

    result = int(''.join([str(x) for x in digits]))

    return result

if __name__ == "__main__":
    main()