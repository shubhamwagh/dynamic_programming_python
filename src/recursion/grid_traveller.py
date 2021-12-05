def grid_traveller(m: int, n: int) -> int:
    """
    :param m: number of rows in grid
    :param n: number of columns in grid
    :return: number of ways to reach bottom right of the grid from a top right corner
    """

    if m == 1 and n == 1:
        # base case
        return 1
    if m == 0 or n == 0:
        # either dims empty no way to travel
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


if __name__ == "__main__":
    print(grid_traveller(2, 3))