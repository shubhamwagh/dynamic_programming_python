from typing import Dict


def fib(n: int) -> int:
    """
    :param n: input integer
    :return: Nth number of fibonacci sequence

    Time complexity : O(2^n)
    Space complexity : O(n)
    """
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    print(fib(6))
    print(fib(7))
    print(fib(8))
