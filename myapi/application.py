import cv2 
from urllib.request import urlopen
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image as kerasIMG
from PIL import Image
#from tensorflow.keras.models import load_model

model = load_model("C:/Users/IsRa.ChaaBani/Desktop/application_brain_tumor_detection/brain-tumor-detection-back/myapi/models/best_model.h5")
print('Model loaded. http://127.0.0.1:8000/')

def get_className(classNo):
    print(classNo)
    if classNo==0:
        return "No Brain Tumor"
    elif classNo==1:
        return "Yes Brain Tumor"
    
 
 
def getResult(img):
    image=cv2.imread(img)
    image = Image.fromarray(image, 'RGB')
    image = image.resize((224, 224))
    image=np.array(image)
    input_img = np.expand_dims(image, axis=0)
    result=model.predict(input_img)
    return result
    

      


"""def make_prediction(img):
    images = []
    req = urlopen(img)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1) # 'Load it as it is'
 
    
    
    img=Image.fromarray(image)
    img=img.resize((224,224))
    img=np.array(img)
    input_img = np.expand_dims(img, axis=0)
    
    res = model.predict(input_img)
    if res:
        print("Tumor Detected")
    else:
        print("No Tumor ")
"""
"""def model_loading(image):
    np_array = np.array(image)
    print(np_array.shape)
    model = load_model('C:/Users/IsRa.ChaaBani/Desktop/application_brain_tumor_detection/brain-tumor-detection-back/myapi/models/model_cnn_1.h5')
    output = model.predict(np_array)
    return output
 """

