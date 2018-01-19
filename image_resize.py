from __future__ import print_function
import argparse
from PIL import Image
import re


def create_parser():
    parser = argparse.ArgumentParser(description='Programm recizes images by input parameters')
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-wh',
                       '--width_height',
                       type=int,
                       nargs='*',
                       help='Width and Heigth of result image')
    group.add_argument('-s', '--scale', type=float, help='Scale of resize')
    return parser


def resize_image(path_to_original, path_to_result, scale, width, height):
    original = Image.open(path_to_original)
    original_width = original.size[0]
    original_height = original.size[1]
    if scale:
        original.resize((original_width*scale, original_height*scale)).save(path_to_result)
    else:
        if not (original_width/original_height) == width/height:
            print('Result image proportion will be changed')
        original.resize((width, height)).save(path_to_result)


def generate_image_name(path_to_original, path_to_result, scale, width, height):
    if not path_to_result:
        print(path_to_original)
    print(re.findall(r'("[]")', path_to_original))



if __name__ == '__main__':
    parser = create_parser()
    options = parser.parse_args() # ['-i G:\\devman\\778845102.jpg','-wh 2 3']
    generate_image_name(options.input, options.output, options.scale, options.width_height[0], options.width_height[1])
    # resize_image(parameters.input, parameters.output, parameters.scale, parameters.)

