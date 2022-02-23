from typing import List


def all_construct(target_str: str, word_bank: List) -> List:
    """
    :param target_str: target string
    :param word_bank: List of words
    :return: List containing all possible ways to generate target_str using words from word_bank.
    """

    if target_str == '':
        return [[]]

    result = []

    for word in word_bank:
        if target_str.startswith(word):
            # rem_string = target_str.replace(str, '')
            suffix = target_str[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[word] + el for el in suffix_ways]
            result.extend(target_ways)
    return result


if __name__ == "__main__":
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purp']))
