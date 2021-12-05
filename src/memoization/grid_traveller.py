from typing import Dict


def grid_traveller(m: int, n: int, memo: Dict = {}) -> int:
    '''
    :param m: number of rows in grid
    :param n: number of columns in grid
    :param memo: memoization i.e. hash map to store intermediate computation results
    :return: number of ways to reach bottom right of the grid from a top right corner given it can only move down or right
    '''
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        # base case
        return 1
    if m == 0 or n == 0:
        # either dims empty no way to travel
        return 0

    memo[key] = grid_traveller(m - 1, n, memo) + grid_traveller(m, n - 1, memo)
    return memo[key]


if __name__ == "__main__":
    print(grid_traveller(18, 18))