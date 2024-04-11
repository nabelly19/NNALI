from utils import *

path = "data\\filters" 
folders = get_folders(path)

def dilate(img):
    return dilate_image(img, (33,33))

def erode(img):
    return erode_image(img, (40,40))

print("erode")
for folder in folders:
    process_images_in_directory(erode, folder, folder)

print("dilate")
for folder in folders:
    process_images_in_directory(dilate, folder, folder)



# img = cv.imread("data\\filters\Z\img036-018.png")
# show(erode(img))
# show(dilate(img))