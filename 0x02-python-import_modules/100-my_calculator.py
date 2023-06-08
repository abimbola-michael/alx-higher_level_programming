#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        optd = {"+": add, "-": sub, "*": mul, "/": div}
        opt = list(optd.keys())
        if sys.argv[2] not in opt:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        a = int(sys.argv[1])
        o = sys.argv[2]
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, o, b, optd[o](a, b)))
