from typing import Dict


def fib(n: int, memo: Dict = {}) -> int:
    """

    :param n: input integer
    :param memo: memoization i.e. hash map to store intermediate computation results
    :return: Nth number of fibonacci sequence
    """

    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(500))
