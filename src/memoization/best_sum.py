from typing import List, Optional, Dict


def best_sum(target_sum: int, nums: List, memo: Dict = {}) -> Optional[List]:
    """
    :param target_sum: non negative target sum
    :param nums: List of non negative numbers
    :param memo: memoization i.e. hash map to store intermediate computation results
    :return: Shortest combination of nums using numbers from the nums list that add up to target_sum.
    """

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in nums:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, nums, memo)
        if remainder_combination is not None:
            combination = remainder_combination.copy()
            combination.append(num)
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


if __name__ == "__main__":
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [1, 4, 5]))
    print(best_sum(100, [1, 2, 5, 25]))