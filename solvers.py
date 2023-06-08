from collections.abc import Callable
import math

def isPrime(n: int):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primeFactor(n: int) -> list[int]:
    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n % 2 == 0:
        return [2] + primeFactor(n // 2)
    
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return [i] + primeFactor(n // i)
    return [n]

Solver = Callable[[], int]

def multiplesOf3Or5():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def evenFibonacciNumbers():
    total = 0
    fibs = [1, 1]
    while fibs[-1] < 4000000:
        next = fibs[-1] + fibs[-2]
        fibs.append(next)
        if next % 2 == 0:
            total += next
    return total

def largestPrimeFactor():
    target = 600851475143
    highestPossible = math.floor(math.sqrt(target))
    for i in range(highestPossible, 2, -1):
        if target % i == 0 and isPrime(i):
            return i
    return 1

def largestPalindromeProduct():
    highest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > highest:
                highest = product
    return highest

def smallestMultiple():
    primeFactors = {}
    for i in range(1, 21):
        factors = primeFactor(i)
        for factor in factors:
            if factor not in primeFactors or primeFactors[factor] < factors.count(factor):
                primeFactors[factor] = factors.count(factor)
    total = 1
    for factor in primeFactors:
        total *= factor ** primeFactors[factor]

    return total

solvers: list[Solver] = [
    multiplesOf3Or5,
    evenFibonacciNumbers,
    largestPrimeFactor,
    largestPalindromeProduct,
    smallestMultiple,
]

def solve(problem: int):
    if (problem > len(solvers)):
        raise Exception("Invalid problem number: too high")
    elif (problem <= 0):
        raise Exception("Invalid problem number: too low")
    return solvers[problem - 1]()