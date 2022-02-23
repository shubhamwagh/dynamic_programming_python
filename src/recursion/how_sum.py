from typing import List, Optional


def how_sum(target_sum: int, nums: List) -> Optional[List]:
    """
    :param target_sum: non negative target sum
    :param nums: List of non negative numbers
    :return: List of nums using numbers from the nums list to generate target_sum.
    """

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in nums:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, nums)
        if remainder_result is not None:
            remainder_result.append(num)
            return remainder_result
    return None


if __name__ == "__main__":
    print(how_sum(7, [2, 3]))