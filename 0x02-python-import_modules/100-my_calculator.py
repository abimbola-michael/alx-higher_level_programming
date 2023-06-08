#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 != 3:
        print"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        operators_dict = {"+":add, "-":sub, "*":mul, "/":div}
        operators = list(operators_dict.keys())
        if sys.arg[2] not in operators:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, operators_dict[sys.argv[2]](a, b)))
