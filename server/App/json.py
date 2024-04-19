from App.src.utils import *
import App.src.predict as predict
from tensorflow.keras import models
from flask import Blueprint
from flask_cors import cross_origin

bp = Blueprint('json', __name__, url_prefix='/predict')
model_path = "./App/model9292(95ms).keras"
model = models.load_model(model_path)

@bp.route('/', methods=['POST', 'GET'])
@cross_origin()
def requisition():
    # print("Current working directory:", os.getcwd())
    image = cv.imread("../winforms/FPS_0.png")
    print(image.shape)
    image = resize_image(image, (480, 270))
    print("khg")
    # show(image)
    return predict.run(image, model, save=True)