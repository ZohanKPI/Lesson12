import concurrent.futures
import math
import timeit


def factorial(n):
    return math.factorial(n)


def calculate_factorial_threadpool(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(factorial, n)
        result = future.result()
    return result


def calculate_factorial_processpool(n):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(factorial, n)
        result = future.result()
    return result


if __name__ == '__main__':
    n = 10
    print(f"Calculating factorial of {n}")

    print("Using ThreadPoolExecutor:")
    print(timeit.timeit(stmt='calculate_factorial_threadpool(n)',
                  setup='from __main__ import calculate_factorial_threadpool, n', number=1))
    calculate_factorial_threadpool(n)

    print("Using ProcessPoolExecutor:")
    print(timeit.timeit(stmt='calculate_factorial_processpool(n)',
                  setup='from __main__ import calculate_factorial_processpool, n', number=1))
    calculate_factorial_processpool(n)