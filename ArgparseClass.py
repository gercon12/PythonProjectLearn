#command line arguments using arc pass module
# Two types of arguments 1)Positional 2)Optional
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number1: ', help="first number", type=int)
    parser.add_argument('number2: ', help="second number", type=int)
    parser.add_argument('operation: ', help="operation", type=str)

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)
