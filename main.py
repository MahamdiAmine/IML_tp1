import cv2
import numpy as np
from PIL import Image


def read_img(path):
    try:
        return cv2.imread(path)
    except IOError as e:
        print(e)
        return None


def display(path):
    img = read_img(path)
    image = cv2.resize(img, (720, 500))
    height, width, channels = img.shape
    title = 'image' + ' width = ' + str(width) + ' height = ' + str(height) + ' channels =' + str(channels)
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert_to_PNG(path, name='output'):
    im = Image.open(path)
    output_path = 'converted_images/' + name + '.png'
    im.save(output_path)


def convert_to_TIFF(path, name='output'):
    im = Image.open(path)
    output_path = 'converted_images/' + name + '.TIFF'
    im.save(output_path)


def display_COL(path, Color):
    img = read_img(path)
    image = cv2.resize(img, (720, 500))
    height, width, channels = img.shape
    title = 'image' + ' width = ' + str(width) + ' height = ' + str(height) + ' channels =' + str(
        channels) + ' color = ' + Color
    if Color == 'Red':
        r = image.copy()
        # set blue and green channels to 0
        r[:, :, 0] = 0
        r[:, :, 1] = 0
        cv2.imshow('Red-RGB', r)
    if Color == 'Green':
        g = image.copy()
        # set blue and red channels to 0
        g[:, :, 0] = 0
        g[:, :, 2] = 0
        cv2.imshow('Green-RGB', g)
    if Color == 'Blue':
        b = image.copy()
        # set green and red channels to 0
        b[:, :, 1] = 0
        b[:, :, 2] = 0
        cv2.imshow('Blue-RGB', b)
    if Color is None:
        cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    display('data/nature.jpeg')
    # convert_to_PNG('data/nature.jpeg')
    # convert_to_TIFF('data/nature.jpeg')
    # display_COL('data/nature.jpeg', 'Blue')
    # display_COL('data/nature.jpeg', 'Green')
    # display_COL('data/nature.jpeg', 'Red')
