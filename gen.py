#!/usr/bin/env python3

' generate silver-horn-king nfts '

import os
import base64


def read_file_data(fpath):
    with open(fpath, 'rb') as f:
        return f.read()


def read_file_text(fpath):
    with open(fpath, 'r') as f:
        return f.read()


def write_file_text(fpath, s):
    with open(fpath, 'w') as f:
        f.write(s)


def b64(data):
    return base64.standard_b64encode(data).decode('utf-8')


def main():
    pwd = os.path.dirname(os.path.abspath(__file__))
    print(f'set pwd: {pwd}')
    svg_base = read_file_text(pwd + '/silver-horn-king.svg')
    for s in os.listdir(pwd):
        if s.endswith('.png'):
            svg_gen = pwd + '/build/shk-' + s[:-4] + '.svg'
            png_data = read_file_data(pwd+'/'+s)
            png_text = b64(png_data)
            gen = svg_base.replace('{COIN}', png_text)
            write_file_text(svg_gen, gen)
            print(f'generated: {svg_gen}')


if __name__ == '__main__':
    main()
