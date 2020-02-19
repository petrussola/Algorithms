import sys


def cookies(n):
    if n == 3:
        return 4
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    elif n == 0:
        return 1
    elif n < 0:
        return 0
    return cookies(n-1) + cookies(n-2) + cookies(n-3) # n = 4 => 4 + 2 + 1 => 7 


print(cookies(int(sys.argv[1])))
