"""Intracts with user and uses pycolor module to convert color codes
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


def reset_arg_value(args: argparse.Namespace, arg_name: str, arg_reset_value):
    """Resets the arg value with the provided value.

    :param args: Namespace object
    :type args: argparse.Namespace
    :param arg_name: Title of the argument to be reset
    :type arg_name: str
    :param arg_reset_value: The value that will be assigned to the argument
    :type arg_reset_value: Any
    :return: None
    """
    _dict = vars(args)
    _dict[arg_name] = arg_reset_value


if __name__ == "__main__":
    args = parser.parse_args()

    c = _pycolor.Color()
    converted_color_code: str

    # Working with dic is more convenient
    args_dict = vars(args)

    if args_dict['hex_to_hsv']:
        # reset the arg value (there should be a better way)
        reset_arg_value(args, 'hex_to_hsv', False)
        print(args_dict['hex_to_hsv'])
        converted_color_code = c.convert_hex_to_hsv(
            # hex code only has one parameter
            args.color_code[0]
        )

    elif args_dict['hex_to_rgb']:
        # reset the arg value
        reset_arg_value(args, 'hex_to_rgb', False)
        print(args_dict['hex_to_rgb'])
        converted_color_code = c.convert_hex_to_rgb(
            # hex code only has one parameter
            args.color_code[0]
        )

    elif args_dict['rgb_to_hsv']:
        # reset the arg value
        reset_arg_value(args, 'rgb_to_hsv', False)
        print(args_dict['rgb_to_hsv'])
        converted_color_code = c.convert_rgb_to_hsv(
            # rgb has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    elif args_dict['rgb_to_hex']:
        # reset the arg value
        reset_arg_value(args, 'rgb_to_hex', False)
        print(args_dict['rgb_to_hex'])
        converted_color_code = c.convert_rgb_to_hex(
            # rgb has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    elif args_dict['hsv_to_rgb']:
        # reset the arg value
        reset_arg_value(args, 'hsv_to_rgb', False)
        print(args_dict['hsv_to_rgb'])
        converted_color_code = c.convert_hsv_to_rgb(
            # hsv has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    elif args_dict['hsv_to_hex']:
        # reset the arg value
        reset_arg_value(args, 'hsv_to_hex', False)
        print(args_dict['hsv_to_hex'])
        converted_color_code = c.convert_hsv_to_hex(
            # hsv has three parameters
            (args.color_code[0], args.color_code[1], args.color_code[2])
        )

    print(converted_color_code)
