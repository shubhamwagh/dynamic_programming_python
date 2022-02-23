from typing import List, Dict


def can_construct(target_str: str, word_bank: List, memo: Dict = {}) -> bool:
    """
    :param target_str: target string
    :param word_bank: List of words
    :param memo: memoization i.e. hash map to store intermediate computation results
    :return: Boolean value if it is possible to generate target_str using words from word_bank.
    """

    if target_str in memo:
        return memo[target_str]
    if target_str == '':
        return True
    for str in word_bank:
        if target_str.startswith(str):
            rem_string = target_str.replace(str, '')
            if can_construct(rem_string, word_bank, memo):
                memo[target_str] = True
                return True
    memo[target_str] = False
    return False


if __name__ == "__main__":
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeee']))