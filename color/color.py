""" Converts color codes
"""

import colorsys
import colour

class Color:
    """ Color class represents a color """
    
    def __init__(self):
        """" Initialize with white color """
        self.hex_code = "FFFFFF"
        self.rgb_code = (255, 255, 255)
        self.hsv_code = (0, 0, 100)


    def convert_hex_to_hsv(self, hex_code):
        rgb_code = colour.hex2rgb(hex_code)
        print(colorsys.rgb_to_hsv(rgb_code.r, rgb_code.g, rgb_code.b))


    def convert_hsv_to_hex(self, hsv_code):
        rgb_code = colorsys.hsv_to_rgb(hsv_code)
        print(colour.rgb2hex(rgb_code))


    def convert_rgb_to_hex(self, rgb_code):
        print(colour.rgb2hex(rgb_code))


    def convert_hex_to_rgb(self, hex_code):
        print(colour.hex2rgb(hex_code))


    def convert_hsv_to_rgb(self, hsv_code):
        print(colorsys.hsv_to_rgb(hsv_code.h, hsv_code.s, hsv_code.v))

    def convert_rgb_to_hsv(self, rgb_code):
        print(colorsys.rgb_to_hsv(rgb_code.r, rgb_code.g, rgb_code.b))

