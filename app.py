""" Intracts with user and uses pycolor module to convert color codes
"""

import argparse
import pycolor.color as _pycolor

#  using argparse package to handle the command line interface (CLI)
#  https://docs.python.org/3.7/library/argparse.html

parser = argparse.ArgumentParser(description='Converts color codes.')

parser.add_argument(
    '--hex_to_hsv',
    action='store_true',
    help='converts hex to hsv')

parser.add_argument(
    '--hex_to_rgb',
    action='store_true',
    help='converts hex to rgb')

parser.add_argument(
    '--rgb_to_hsv',
    action='store_true',
    help='converts rgb to hsv')

parser.add_argument(
    '--rgb_to_hex',
    action='store_true',
    help='converts rgb to hex')

parser.add_argument(
    '--hsv_to_rgb',
    action='store_true',
    help='converts hsv to rgb')

parser.add_argument(
    '--hsv_to_hex',
    action='store_true',
    help='converts hsv to hex')

parser.add_argument(
    'color_code',
    metavar='color_code',
    nargs='+',
    help='color code')


if __name__ == "__main__":
    args = parser.parse_args()

    c = _pycolor.Color()
    converted_color_code: str

    if args.__contains__('hex_to_hsv'):
        converted_color_code = c.convert_hex_to_hsv(
            # hex code only has one parameter
            args.color_code[0]
        )

    elif args.__contains__('hex_to_rgb'):
        converted_color_code = c.convert_hex_to_rgb(
            # hex code only has one parameter
            args.color_code[0]
        )

    elif args.__contains__('rgb_to_hsv'):
        converted_color_code = c.convert_rgb_to_hsv(
            # rgb has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    elif args.__contains__('rgb_to_hex'):
        converted_color_code = c.convert_rgb_to_hex(
            # rgb has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    elif args.__contains__('hsv_to_rgb'):
        converted_color_code = c.convert_hsv_to_rgb(
            # hsv has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    elif args.__contains__('hsv_to_hex'):
        converted_color_code = c.convert_hsv_to_hex(
            # hsv has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    print(converted_color_code)
