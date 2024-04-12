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


image = cv.imread("data\\resize\\0\-132301893933691436.jpg")
image = binary(image)

squares = []
for row in range(len(image)):
    print(row)
    for column in range(len(image[row])):
        if(image[row, column] != 0):
            continue
        square = flood_fill(image, column, row)
        if(square in squares):
            continue
        squares.append(square)

print(square)
crop = cv.rectangle(image, square[0], square[1], (0, 255, 0), 2)
crop = cv.getRectSubPix(image, square[0], (40, 70))
show(crop)
# flood_fill(image, 10, 10)


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