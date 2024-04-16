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

    squares = remove_noise(squares)
    squares = organize_letters(squares)

    image = cv.imread(filename)
    if background_color == 0:
        image = invert_mask(image)
        background_color = 255

    circle_image = image.copy()
    for i in range(len(squares)):
        square = squares[i]
        circle_image = cv.rectangle(circle_image, square[0], square[1], (0, 255, 0), 2)
        cropped = crop(square, binary(image.copy()))
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


def organize_letters(squares):
    squares = sorted(squares, key=get_x0)
    return squares


def remove_noise(squares, tol=0.2):
    areas = []

    for square in squares:
        width = square[1][0] - square[0][0]
        height = square[1][1] - square[0][1]
        areas.append(width * height)

    avg_area = sum(areas) / len(areas)
    filtered_squares = filter(lambda idx: areas[idx] >= tol * avg_area, range(len(squares)))
    
    return [squares[idx] for idx in filtered_squares]


def get_x0(square):
    return square[0][0]
