import hashlib
import os
import cv2 as cv


def get_folders(path):
    """
    Get a list of paths for all folders within the specified directory.

    Parameters
    ----------
    path : str
        The path to the directory to be examined.

    Returns
    -------
    list
        A list of paths for all folders within the specified directory.
    """
    folders = []
    items = os.listdir(path)
    for item in items:
        if os.path.isdir(os.path.join(path, item)):
            folders.append(os.path.join(path, item))
    return folders


def process_images_in_directory(
    process_function: callable, source_directory: str, target_directory: str
):
    """
    Process all images in a source directory using a specified processing function
    and save the processed images to a target directory.

    Parameters
    ----------
    process_function : callable
        The function to apply to each image.
    source_directory : str
        The directory containing the original images.
    target_directory : str
        The directory where the processed images will be saved.
    """
    for image_file in os.listdir(source_directory):
        source_filepath = os.path.join(source_directory, image_file)
        image = cv.imread(source_filepath)
        target_filepath = generate_hashed_filename(image, target_directory)
        processed_image = process_function(image)
        if not cv.imwrite(target_filepath, processed_image):
            print("Failed to write image:", source_filepath)


def generate_hashed_filename(img, target_directory):
    """
    Generate a hashed filename for an image based on its content.

    Parameters
    ----------
    img : numpy.ndarray
        The image data.
    target_directory : str
        The directory where the hashed filename will be saved.

    Returns
    -------
    str
        The hashed filename.
    """
    image_bytes = cv.imencode(".jpg", img)[1].tobytes()
    target_filepath = os.path.join(
        target_directory, f"{generate_hash(image_bytes)}.jpg"
    )
    return target_filepath


def generate_hash(data):
    """
    Generate an MD5 hash from input data.

    Parameters
    ----------
    data : bytes
        The data to be hashed.

    Returns
    -------
    str
        The hexadecimal representation of the MD5 hash.
    """
    hash_object = hashlib.md5(data)
    return hash_object.hexdigest()
