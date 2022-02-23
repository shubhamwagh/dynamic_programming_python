from typing import List


def count_construct(target_str: str, word_bank: List) -> int:
    """
    :param target_str: target string
    :param word_bank: List of words
    :return: total number of ways to generate target_str using words from word_bank.
    """

    if target_str == '':
        return 1
    num_ways = 0
    for word in word_bank:
        if target_str.startswith(word):
            # rem_string = target_str.replace(str, '')
            rem_string = target_str[len(word):]
            num_ways += count_construct(rem_string, word_bank)
    return num_ways


if __name__ == "__main__":
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                          ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeee']))
