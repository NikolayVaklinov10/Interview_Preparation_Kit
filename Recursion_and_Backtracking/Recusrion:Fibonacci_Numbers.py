# recursive method with using explicit cache

cache = {}

def fibonacci(num):
    '''Return a fibonacci value of num'''

    if num in cache:
        return cache[num]

    if num == 0:
        result = 0
    elif num == 1 or num == 2:
        result = 1
    else:
        result = fibonacci(num - 2) + fibonacci(num - 1)

    cache[num] = result
    return result
