#Exercise: Commandline Argument Processing using argparse

#    Take subject marks as command line arguments

#example:
#    python3 cmd.py --physics 60 --chemistry 70 --maths 90

#    Find average marks for the three subjects using command line input of marks.
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--physics', help="physics class note", type=int)
    parser.add_argument('--chemistry', help="chemistry class note", type=int)
    parser.add_argument('--maths', help="maths class note", type=int)

    args = parser.parse_args()

    print(args.physics)
    print(args.chemistry)
    print(args.maths)

    average = round((args.physics + args.chemistry + args.maths)/3,2)
    print("average: ",average)
