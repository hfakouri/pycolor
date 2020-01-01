""" Converts color codes
"""

import colorsys
import colour


class Color:
    """ Color class represents a color
    """

    # Added to make the class static
    def __init__(self):

        # Initialize with white color
        self.hex_code = "#FFFFFF"
        self.rgb_code = (255, 255, 255)
        self.hsv_code = (0, 0, 100)

    # Converts HEX color code to HSV color code
    def convert_hex_to_hsv(self, hex_code):
        rgb_code = colour.hex2rgb(hex_code)
        return colorsys.rgb_to_hsv(rgb_code[0], rgb_code[1], rgb_code[2])

    # Converts HSV color code to HEX color code
    def convert_hsv_to_hex(self, hsv_code):
        rgb_code = colorsys.hsv_to_rgb(hsv_code)
        return colour.rgb2hex(rgb_code)

    # Converts RGB color code to HEX color code
    def convert_rgb_to_hex(self, rgb_code):
        return colour.rgb2hex(rgb_code)

    # Converts HEX color code to RGB color code
    def convert_hex_to_rgb(self, hex_code):
        return colour.hex2rgb(hex_code)

    # Converts HSV color code to RGB color code
    def convert_hsv_to_rgb(self, hsv_code):
        return colorsys.hsv_to_rgb(hsv_code[0], hsv_code[1], hsv_code[2])

    # Converts RGB color code to HSV color code
    def convert_rgb_to_hsv(self, rgb_code):
        return colorsys.rgb_to_hsv(rgb_code[0], rgb_code[1], rgb_code[2])
