import sys


def cookies(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    return cookies(n-1) + cookies(n-2) + cookies(n-3)


print(cookies(int(sys.argv[1])))
