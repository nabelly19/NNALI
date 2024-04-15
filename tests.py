
from src.utils import *

# path = "data\\filters" 
# folders = get_folders(path)

# array = []

# for folder in folders:
#     print(folder)
#     count = 0
#     for image_file in os.listdir(folder):
#         source_filepath = os.path.join(folder, image_file)
#         # print(source_filepath)
#         image = cv.imread(source_filepath)
#         # print(cv.imwrite(".png",image))
#         count += 1
#     array.append(folder + " | "+ str(count))

# print (array)


image = cv.imread("data\\filters\\0\-73854686951403631.jpg")
show(resize_image(image))