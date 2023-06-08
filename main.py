import sys
from solvers import solve

if __name__ == "__main__":
    problem = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    total = solve(problem)
    print(total)