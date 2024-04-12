from utils import *

path = "data\\filters" 
target_path = "data\\resize" 
folders = get_folders(path)
target_folders = get_folders(target_path)

def dilate(img):
    return dilate_image(img, (33,33))

def erode(img):
    return erode_image(img, (40,40))

# print("erode")
# for folder in folders:
#     process_images_in_directory(erode, folder, folder)

# print("dilate")
# for folder in folders:
    process_images_in_directory(dilate, folder, folder)

print("resize")
for folder, target_folder in zip(folders, target_folders):
    process_images_in_directory(resize_image, folder, target_folder)



# img = cv.imread("data\\filters\Z\img036-018.png")
# show(erode(img))
# show(dilate(img))