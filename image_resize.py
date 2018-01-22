import argparse
import os
from PIL import Image


def create_parser():
    parser = argparse.ArgumentParser(
        description='Program resizes images by input parameters')
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-wh',
                       '--width_height',
                       type=int,
                       nargs='*',
                       help='Width and height of result image')
    group.add_argument('-s', '--scale', type=float, help='Scale of resize')
    return parser


def resize_image(path_to_original, path_to_result, scale, width_height):
    original = Image.open(path_to_original)
    original_width = original.size[0]
    original_height = original.size[1]
    if scale:
        original.resize((
            original_width*scale,
            original_height*scale
        )).save(path_to_result)
    else:
        width = width_height[0]
        height = width_height[1]
        if not (original_width/original_height) == width/height:
            print('Result image proportion will be changed')
        original.resize((
            width_height[0],
            width_height[1]
        )).save(path_to_result)


def generate_image_name(path_to_original, path_to_result, scale, width_height):
    (original_root, original_file_name) = os.path.split(path_to_original)
    (original_prefix_name,
     original_extension) = os.path.splitext(original_file_name)
    if scale:
        result_name = '{}__x{}{}'.format(
            original_prefix_name,
            str(scale),
            original_extension)
    else:
        width = width_height[0]
        height = width_height[1]
        result_name = '{}__{}x{}{}'.format(
            original_prefix_name,
            str(width),
            str(height),
            original_extension)
    if path_to_result:
        if not os.path.splitext(path_to_result)[1]:
            return os.path.join(path_to_result, result_name)
        else:
            return path_to_result
    else:
        return os.path.join(original_root, result_name)


if __name__ == '__main__':
    parser = create_parser()
    options = parser.parse_args()
    path_to_result = generate_image_name(
        options.input,
        options.output,
        options.scale,
        options.width_height)
    resize_image(
        options.input,
        path_to_result,
        options.scale,
        options.width_height)
