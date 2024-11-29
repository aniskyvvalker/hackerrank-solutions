import textwrap

def wrap(string, max_width):
    if (0 < len(string) < 1000) and (0 < max_width < len(string)):
        return "\n".join(textwrap.wrap(string, width=max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)