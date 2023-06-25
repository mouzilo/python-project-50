#!/usr/bin/env python3

import argparse
from gendiff.scripts.gendiff_json import gendiff_json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--f', '--format', metavar='FORMAT',
                        type=str, help='set format for output')
    args = parser.parse_args()

    file1 = args.first_file
    file2 = args.second_file
    return gendiff_json(file1, file2)


if __name__ == '__main__':
    main()
