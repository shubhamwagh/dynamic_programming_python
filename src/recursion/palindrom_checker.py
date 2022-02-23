def is_palindrome(string : str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:len(string) - 1])
    return False

if __name__ == "__main__":
    print(is_palindrome("Shubham"))