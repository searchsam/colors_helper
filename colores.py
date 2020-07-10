#!/usr/bin/python3

import sys


def hex_to_rgb(hex):
    return tuple(map(lambda x: int(hex[x : x + 2], 16), (0, 2, 4)))


def rgb_to_hex(rgb):
    return "#%02x%02x%02x".upper() % rgb


def transform_color(rgb):
    rgb_light = tuple([111, 139, 251])
    rgb_dark = tuple([89, 120, 243])
    rgb_new = list()

    for count, color in enumerate(rgb):
        tmp = int((color * rgb_light[count]) / rgb_dark[count])
        if tmp > 255:
            tmp = 255
        rgb_new.append(tmp)

    return tuple(rgb_new)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        hex = sys.argv[1]
        rgb = hex_to_rgb(hex)
        print("#" + hex, rgb)
        new_rgb = transform_color(rgb)
        new_hex = rgb_to_hex(new_rgb)
        print(new_hex, new_rgb)
    else:
        print('Verifique que el valor HEX que introdujo no lleve "#" al inicio.')
        sys.exit(1)
