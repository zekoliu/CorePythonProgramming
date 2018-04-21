
def safe_input():
    try:
        input_str = raw_input("Enter a string: ")
    except (EOFError, KeyboardInterrupt), e:
        print e
        return None
    return input_str

if __name__ == '__main__':
    safe_input()