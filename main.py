from collections.abc import Callable
import sys
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

if __name__ == "__main__":
    solvers: list[Solver] = [
        multiplesOf3Or5,
        evenFibonacciNumbers,
        largestPrimeFactor,
    ]
    problem = 0 if len(sys.argv) < 2 else int(sys.argv[1]) - 1
    if (problem >= len(solvers)):
        print("Invalid problem number: too high")
        exit(1)
    elif (problem < 0):
        print("Invalid problem number: too low")
        exit(1)
    total = solvers[problem]()
    print(total)