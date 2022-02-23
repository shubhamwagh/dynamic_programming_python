def string_reversal(string: str) -> str:
    if string == '':
        return ''
    return string_reversal(string[1:]) + string[0]


if __name__ == "__main__":
    print(string_reversal("My name is Shubham"))
