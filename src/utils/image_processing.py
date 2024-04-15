from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np
from .data_processing import *

def show(img):
    """
    Display an image using Matplotlib.

    Parameters
    ----------
    img : array_like
        The image to be displayed.
    """
    plt.imshow(img, cmap="gray")
    plt.show()


def binary(img, method=cv.THRESH_OTSU):
    """
    Convert an image to binary using a specified thresholding method.

    Parameters
    ----------
    img : array_like
        The input image.
    method : int, optional
        The thresholding method to be used (default is cv.THRESH_OTSU).

    Returns
    -------
    numpy.ndarray
        The binary image.
    """
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img = cv.threshold(img, 80, 255, method)
    return img


def erode_image(img, kernel_size=(42, 42)):
    """
    Perform erosion operation on an image.

    Parameters
    ----------
    img : numpy.ndarray
        The input image.
    kernel_size : tuple, optional
        Size of the structuring element for erosion (default is (2, 2)).

    Returns
    -------
    numpy.ndarray
        The eroded image.
    """
    kernel = np.ones(kernel_size, np.uint8)
    eroded_img = cv.erode(img, kernel)
    return eroded_img


def dilate_image(img, kernel_size=(43, 43)):
    """
    Perform dilation operation on an image.

    Parameters
    ----------
    img : numpy.ndarray
        The input image.
    kernel_size : tuple, optional
        Size of the structuring element for dilation (default is (3, 3)).

    Returns
    -------
    numpy.ndarray
        The dilated image.
    """
    kernel = np.ones(kernel_size, np.uint8)
    dilated_img = cv.dilate(img, kernel)
    return dilated_img


def resize_image(img, new_size=(120, 90)):
    """
    Resize an image to a new size.

    Parameters
    ----------
    img : numpy.ndarray
        The input image.
    new_size : tuple, optional
        The new size to resize the image to (default is (128, 128)).

    Returns
    -------
    numpy.ndarray
        The resized image.
    """
    return cv.resize(img, new_size)


def flood_fill(img, x, y):
    """
    Perform flood fill operation on an image.

    Parameters
    ----------
    img : numpy.ndarray
        The input image.
    x : int
        The x-coordinate of the seed point.
    y : int
        The y-coordinate of the seed point.

    Returns
    -------
    tuple
        A tuple containing the coordinates of the bounding box surrounding the filled area.
    """
    max_y, max_x = img.shape
    color = img[y][x]

    x0 = xf = x
    y0 = yf = y

    if not (0 <= y < max_y) or not (0 <= x < max_x):
        return None

    queue = [(x, y)]
    visited = set()

    while queue:
        curr_x, curr_y = queue.pop()

        if (0 > curr_y or curr_y >= max_y) or (0 > curr_x or curr_x >= max_x):
            continue

        if (curr_x, curr_y) in visited:
            continue

        visited.add((curr_x, curr_y))

        if img[curr_y][curr_x] != color:
            continue

        x0 = min(x0, curr_x)
        xf = max(xf, curr_x)

        y0 = min(y0, curr_y)
        yf = max(yf, curr_y)

        queue.append((curr_x + 1, curr_y))
        queue.append((curr_x - 1, curr_y))
        queue.append((curr_x, curr_y + 1))
        queue.append((curr_x, curr_y - 1))

    return ((x0, y0), (xf, yf))


def find_background_color(img):
    """
    Find the background color in a binary image.

    Parameters
    ----------
    img : numpy.ndarray
        The binary image.

    Returns
    -------
    int
        The background color value (0 for black, 255 for white).
    """
    num_white_pixels = np.sum(img == 255)
    num_black_pixels = np.sum(img == 0)

    if num_white_pixels > num_black_pixels:
        background_color = 255
    else:
        background_color = 0

    return background_color


def crop(square, img):
    """
    Crop an image using the specified square coordinates.

    Parameters
    ----------
    square : tuple
        A tuple containing the coordinates of the top-left and bottom-right corners of the square.
    img : numpy.ndarray
        The input image.

    Returns
    -------
    numpy.ndarray
        The cropped image.
    """
    return img[square[0][1] : square[1][1], square[0][0] : square[1][0]]

def save_images(imgs, target_directory):
    """
    Save a list of images to a target directory.

    Parameters
    ----------
    imgs : list
        A list of images to be saved.
    target_directory : str
        The directory where the images will be saved.
    """
    for img in imgs:
        target_filepath = generate_hashed_filename(img, target_directory)
        if not cv.imwrite(target_filepath, img):
            print("Failed to save image.")