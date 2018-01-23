import argparse
import os
import pandas as pd
from PIL import Image
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        description='Program resizes images by input parameters')
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output')
    parser.add_argument('-w', '--width', type=int)
    parser.add_argument('-he', '--height', type=int)
    parser.add_argument('-s', '--scale', type=float)
    return parser


def resize_image(original, scale, width, height):
    orig_width = original.size[0]
    orig_height = original.size[1]
    if not ((orig_width/orig_height) == (width + 1) / (height + 1)) and scale:
        print('Result image proportion will be changed')
    return original.resize((
            width + int(orig_width*scale),
            height + int(orig_height*scale)
        ))


def generate_image_name(path_to_original,
                        path_to_result,
                        scale,
                        width,
                        height):
    (result_root, result_name) = os.path.split(path_to_result)
    (result_prefix_name,
     result_extension) = os.path.splitext(result_name)
    (original_prefix_name,
     original_extension) = os.path.splitext(path_to_original)
    if not result_extension:
        result_prefix_name = original_prefix_name
    result_extension = original_extension
    if scale:
        description = 'x{}'.format(scale)
    else:
        description = '{}x{}'.format(width, height)
    result_name = '{}__{}{}'.format(
        result_prefix_name,
        description,
        result_extension)
    return result_name


if __name__ == '__main__':
    parser = create_parser()
    args_namespace = parser.parse_args()
    options = {
        'input': args_namespace.input,
        'output': args_namespace.output,
        'scale': args_namespace.scale,
        'width': args_namespace.width,
        'height': args_namespace.height
    }
    for key in options:
        if not key == 'output' and options[key] is None:
            options[key] = 0
    if int(options['scale']) and (options['width'] or options['height']):
        sys.exit('Mutually exclusive options. '
                 'Please input scale OR (height AND/OR width)')
    path_to_result = generate_image_name(
        options['input'],
        options['output'],
        options['scale'],
        options['width'],
        options['height'])
    original = Image.open(options['input'])
    result_image = resize_image(
        original,
        options['scale'],
        options['width'],
        options['height'])
    result_image.save(path_to_result)
