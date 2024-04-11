from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np


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


# filepath = "data\Img\\0\img001-001.png"

# image = cv.imread(filepath)
# image = binary(image, dilate=True)
# show(image)
# image = cv.imread(filepath)
# image = binary(image)
# show(image)
# image = cv.imread(filepath)
# image = binary(image, erode=True)
# show(image)
