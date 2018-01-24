import argparse
import os
from PIL import Image
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        description='Program resizes images by input parameters')
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', default='')
    parser.add_argument('-w', '--width', type=int, default=0)
    parser.add_argument('-he', '--height', type=int, default=0)
    parser.add_argument('-s', '--scale', type=float, default=0)
    return parser


def resize_image(original, scale, width, height):
    orig_width, orig_height = original.size
    if not scale:
        if width == 0:
            width = orig_width
        if height == 0:
            height = orig_height
        if not orig_width/orig_height == width/height:
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
    original_prefix_name, original_extension = os.path.splitext(
        path_to_original)
    if not path_to_result:
        path_to_result = original_prefix_name
    if scale:
        description = '_sc'
    else:
        description = '{}x{}'.format(width, height)
    return '{}__{}{}'.format(
        path_to_result,
        description,
        original_extension)


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
    if options['scale'] and (float(options['width']) or float(options['height'])):
        sys.exit('Mutually exclusive options. '
                 'Please input scale OR (height AND/OR width)')
    if os.path.splitext(options['output'])[1] == '':
        path_to_result = generate_image_name(
            options['input'],
            options['output'],
            options['scale'],
            options['width'],
            options['height'])
    else:
        path_to_result = options['output']
    original_image = Image.open(options['input'])
    result_image = resize_image(
        original_image,
        options['scale'],
        options['width'],
        options['height'])
    result_image.save(path_to_result)
