from src.utils import *

letters = get_letters("data\\teste.png")


for i in range(len(letters)):
    letters[i] = resize_image(letters[i])
save_images(letters, "data\letters")

from tensorflow.keras import models

model_path = "pynet\checkpoints\good_model\model9491.keras"
model = models.load_model(model_path)

filename = "data\letters\8937997be3e5cb13fb26dea55abba412.jpg"
image = cv.imread(filename)

image_predict = binary(image)
print(model.predict(image_predict))
