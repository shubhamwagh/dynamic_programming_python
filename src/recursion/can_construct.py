from typing import List


def can_construct(target_str: str, word_bank: List) -> bool:
    """
    :param target_str: target string
    :param word_bank: List of words
    :return: Boolean value if it is possible to generate target_str using words from word_bank.
    """

    if target_str == '':
        return True
    for word in word_bank:
        if target_str.startswith(word):
            # rem_string = target_str.replace(str, '')
            rem_string = target_str[len(word):]
            if can_construct(rem_string, word_bank):
                return True
    return False


if __name__ == "__main__":
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee', 'eeeeeeee']))