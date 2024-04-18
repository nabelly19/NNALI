import src.predict as predict
from tensorflow.keras import models
from src.utils import *
import sys

model_path = "C:/Users/disrct/Desktop/nnali/neuralnet/checkpoints/good_model/model9292(95ms).keras"
model = models.load_model(model_path)

# def main():
image = cv.imread("C:/Users/disrct/Desktop/nnali/winforms/FPS_0.png")
print(image.shape)
image = resize_image(image, (480, 270))
show(image)
sys.stdout.write(predict.run(image, model, save=True))
sys.stdout.flush()

# if __name__ == "__main__":
#     main()