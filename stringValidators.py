if __name__ == '__main__':
    s = input("")
    """
    # Longer way
    s_alnum = "False"
    for char in s:
        if char.isalnum():
            s_alnum = "True"
            break
    print(s_alnum)
    """
    print("True" if any(char.isalnum() for char in s) else "False")
    print("True" if any(char.isalpha() for char in s) else "False")
    print("True" if any(char.isdigit() for char in s) else "False")
    print("True" if any(char.islower() for char in s) else "False")
    print("True" if any(char.isupper() for char in s) else "False")
