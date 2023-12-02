import cv2 
from urllib.request import urlopen
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image as kerasIMG

def processing(img_url):
    images = []
    req = urlopen(img_url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1) # 'Load it as it is'

    if image is not None:
        
        new_size = (200, 200)
        resized_img = cv2.resize(image, new_size)
        normalized_image = resized_img.astype('float32') / 255.0
        images.append(normalized_image)
        return images




def model_loading(image):
    np_array = np.array(image)
    print(np_array.shape)
    vgg16_model = load_model('C:/Users/HP PAVILION/Documents/codecolab/challenges/datascience/api_braintumor_detection/api_tumor_detection/myapi\models/model_VGG16.h5')
    output = vgg16_model.predict(np_array)
    return output
    