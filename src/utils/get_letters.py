from .image_processing import *
import cv2 as cv


def get_letters(filename):
    """
    Extract individual letters from an image.

    Parameters
    ----------
    filename : str
        The filename of the image containing the letters.

    Returns
    -------
    list
        A list of cropped images containing individual letters.
    """
    images_bordered = []
    image = cv.imread(filename)
    image = binary(image)

    background_color = find_background_color(image)

    squares = []
    for row in range(len(image)):
        for column in range(len(image[row])):
            if image[row, column] == background_color:
                continue
            square = flood_fill(image, column, row)
            if square in squares:
                continue
            squares.append(square)

    image = cv.imread(filename)
    circle_image = image.copy()
    for i in range(len(squares)):
        square = squares[i]
        circle_image = cv.rectangle(circle_image, square[0], square[1], (0, 255, 0), 2)
        cropped = crop(square, image.copy())
        image_bordered = cv.copyMakeBorder(
            src=cropped,
            top=10,
            bottom=10,
            left=15,
            right=15,
            borderType=cv.BORDER_CONSTANT,
            value=(background_color, background_color, background_color),
        )
        images_bordered.append(image_bordered)
    show(circle_image)
    return images_bordered
