#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    if l == 1:
        str1 = "argument:"
    elif l == 0:
        str1 = "arguments."
    else:
        str1 = "arguments:"
    print("{:d} {}".format(l, str1))
    for x in range(1, l + 1):
        print("{:d}: {}".format(x, sys.argv[x]))
