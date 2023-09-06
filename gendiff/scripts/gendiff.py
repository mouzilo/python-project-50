#!/usr/bin/env python3

import argparse
import os
from gendiff.parser.parse_files import parse_files


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        type=str, default='stylish',
                        help='set format for output (default: stylish)')
    args = parser.parse_args()

    base_dir = os.path.join(os.getcwd(), 'files')
    file1 = os.path.join(base_dir, args.first_file)
    file2 = os.path.join(base_dir, args.second_file)

    result = parse_files(file1, file2)

    if args.format == 'stylish':
        print(result)
    elif args.format == 'json':
        import json
        print(json.dumps(result, indent=4))
    else:
        raise ValueError(f"Unsupported output format: {args.format}")


if __name__ == '__main__':
    main()
