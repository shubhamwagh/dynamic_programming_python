from typing import List, Dict


def can_sum(target_sum: int, nums: List, memo: Dict = {}) -> bool:
    """
    :param target_sum: non negative target sum
    :param nums: List of non negative numbers
    :param memo: memoization i.e. hash map to store intermediate computation results
    :return: Boolean value if it is possible to generate target_sum using numbers from the nums list.
    """
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in nums:
        remainder = target_sum - num
        if can_sum(remainder, nums, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


if __name__ == "__main__":
    print(can_sum(300, [7, 14]))