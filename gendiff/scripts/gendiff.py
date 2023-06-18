import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--f', '--format', metavar='FORMAT',
                        type=str, help='set format for output')
    args = parser.parse_args()
    return args.first_file


if __name__ == '__main__':
    main()
