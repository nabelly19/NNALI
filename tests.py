import src.predict as predict
from tensorflow.keras import models

from src.utils import *

model_path = "neuralnet\checkpoints\good_model\model9292(95ms).keras"
model = models.load_model(model_path)
# print(predict.run("data\\teste2.png", model))
# print(predict.run("data\\teste.png", model))
# print(predict.run("data\inquisicao_crop_edit.png", model, save=True))
print(predict.run(cv.imread("data\inquisicao_crop.png"), model, save=True))

# image = cv.imread("data\inquisicao_crop_edit.png")
# image = binary(image)
# show(image)