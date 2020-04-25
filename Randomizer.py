from random import randint


def random(n):
    start = 10**(n-1)
    end = (10**n)-1
    return randint(start, end)

print random(4)
