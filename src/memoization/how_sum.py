from typing import List, Optional, Dict


def how_sum(target_sum: int, nums: List, memo: Dict = {}) -> Optional[List]:
    """
    :param target_sum: non negative target sum
    :param nums: List of non negative numbers
    :param memo: memoization i.e. hash map to store intermediate computation results
    :return: List of nums using numbers from the nums list to generate target_sum.
    """

    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in nums:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, nums, memo)
        if remainder_result is not None:
            remainder_result.append(num)
            memo[target_sum] = remainder_result
            return remainder_result
    memo[target_sum] = None
    return None


if __name__ == "__main__":
    print(how_sum(7, [2, 3]))
    print(how_sum(300, [7, 14]))