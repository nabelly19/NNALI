from datetime import datetime
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


def process_images_in_directory(process_function: callable, source_directory: str, target_directory: str):
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
        image_bytes = cv.imencode('.jpg', image)[1].tobytes()
        target_filepath = os.path.join(target_directory, f"{hash(image_bytes)}.jpg")
        processed_image = process_function(image)
        if not cv.imwrite(target_filepath, processed_image):
            print("False: ", source_filepath)

def generate_hash(data):
    hash_object = hashlib.md5(data)
    return hash_object.hexdigest()
        