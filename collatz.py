#!/usr/bin/python3

def collatz(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        return collatz(int(n / 2))
    else:
        return collatz(int(3 * n + 1))


if __name__ == "__main__":
    try:
        n = int(input())
        collatz(n)
        
    except Exception:
        print('Prease enter an integer.')
