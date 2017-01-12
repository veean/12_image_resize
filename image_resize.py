from PIL import Image
import argparse
import os
import sys


def get_arguments_for_resize():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='path to initial image')
    parser.add_argument('-w', '--width', type=int)
    parser.add_argument('-ht', '--height', type=int)
    parser.add_argument('-s', '--scale', type=float)
    parser.add_argument('-o', '--output')
    return parser.parse_args()


def resize_image(original_image, resized_width=None, resized_height=None):
    source_width, source_height = original_image.size
    if resized_width and resized_height:
        break_keep_ratio = round(source_width / source_height, 2) != round(resized_width / resized_height, 2)
        if break_keep_ratio:
            print("Width/Height ratio won't match with the original image!")
    else:
        resized_width = resized_width if resized_width else round(resized_height / source_height * source_width)
        resized_height = resized_height if resized_height else round(resized_width / source_width * source_height)
    return original_image.resize((resized_width, resized_height))


def scale_image(image, scale_size):
    image_width, image_height = image.size
    return image.resize((round(image_width * scale_size), round(image_height * scale_size)))


def save_image_to_path(image, from_source_path, to_filepath=None):
    if to_filepath:
        image.save(to_filepath, image.format)
    else:
        source_dir, source_extension = os.path.splitext(from_source_path)
        to_filepath = '{}__{}x{}{}'.format(source_dir, image.size[0], image.size[1], source_extension)
        image.save(to_filepath, image.format)


def catch_errors(parser_args):
    if parser_args.scale and any([parser_args.height, parser_args.width]):
        sys.exit("Can't be scale and [width or height] parameters at once!")
    if not os.path.exists(parser_args.file):
        sys.exit("{} doesn't exist!".format(parser_args.file))


if __name__ == '__main__':
    parameters = get_arguments_for_resize()
    catch_errors(parameters)
    target_image = Image.open(parameters.file)

    if parameters.scale:
        target_image = scale_image(target_image, parameters.scale)
    elif parameters.width or parameters.height:
        target_image = resize_image(target_image, parameters.width, parameters.height)
    save_image_to_path(target_image, parameters.file, parameters.output)
