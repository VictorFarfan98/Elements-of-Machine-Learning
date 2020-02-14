import time
#from memoizaition import cached


# @cached
def factorial(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
        time.sleep(1)
    return fact


# print(factorial(5))


# lambda n: return reduce(lambda a, b: a * b, range(n, 1, -1))

cache = {}


def memoize(slow_function, param):
    try:
        return dic[param]
    except:
        cache[param] = slow_function(param)
        return cache[param]


print(memoize(factorial, 5))
print(memoize(factorial, 5))
