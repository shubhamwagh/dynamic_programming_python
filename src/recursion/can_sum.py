from typing import List


def can_sum(target_sum: int, nums: List) -> bool:
    """
    :param target_sum: non negative target sum
    :param nums: List of non negative numbers
    :return: Boolean value if it is possible to generate target_sum using numbers from the nums list.
    """

    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for num in nums:
        remainder = target_sum - num
        if can_sum(remainder, nums):
            return True
    return False


if __name__ == "__main__":
    print(can_sum(7, [5, 3, 4, 7]))