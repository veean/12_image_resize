from PIL import Image
import argparse
import os




def get_arguments_for_resize():
    parser = argparse.ArgumentParser(description='Output file for information about <Coursera> courses')
    parser.add_argument('file', type=str, help='path to initial image')
    parser.add_argument('-w', '--width', type=int)
    parser.add_argument('-H', '--height', type=int)
    parser.add_argument('-s', '--scale', type=float)
    parser.add_argument('-o', '--output')
    return parser.parse_args()


def open_image(path_to_image):
    if os.path.exists(path_to_image):
        return Image.open(path_to_image)


def resize_image(original_image, resized_width, resized_height):
    source_width, source_height = original_image.size
    if resized_width and resized_height:
        break_keep_ratio = round(source_width / source_height, 2) != round(resized_width / resized_height, 2)
        if break_keep_ratio:
            print("Ratio won't match with the original image!")
        # return original_image.resize(resized_width, resized_height)
    else:
        resized_width = resized_width if resized_width else


    return original_image.resize(resized_width, resized_height)

def scale_image(image, scale_size):
    image_width, image_height = image.size
    return image.resize(round(image_width * scale_size), round(image_height * scale_size))


def save_image_to_path(image, from_source_path, to_filepath):
    if to_filepath and os.path.exists(to_filepath):
        image.save(to_filepath, image.format)


# C:\Users\Vadim\Desktop\TShoot\Screens\test\sharepoint_privilegies.png
if __name__ == '__main__':
    parameters = get_arguments_for_resize()
    if parameters.scale and any([parameters.width, parameters.height]):

