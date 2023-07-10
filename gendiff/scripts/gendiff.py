#!/usr/bin/env python3

import argparse
import os
from gendiff.scripts.gendiff_json import gendiff_json


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('--f', '--format', metavar='FORMAT',
                        type=str, help='set format for output')
    args = parser.parse_args()

    base_dir = os.path.join(os.getcwd(), 'files')
    file1 = os.path.join(base_dir, args.first_file)
    file2 = os.path.join(base_dir, args.second_file)
    result = gendiff_json(file1, file2)
    print(result)


if __name__ == '__main__':
    main()
