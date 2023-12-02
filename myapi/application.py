import cv2 
from urllib.request import urlopen
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image as kerasIMG
from PIL import Image

"""def processing(img_url):
    images = []
    req = urlopen(img_url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1) # 'Load it as it is'

    
    img = cv2.imread(image)
    img = Image.fromarray(img)
    img = img.resize((224, 224))
    img = np.array(img)
    input_img = np.expand_dims(img, axis=0)
    return input_img     
"""
from PIL import Image
 
def convert_tiff_to_png(input_path, output_path):
    # Open the TIFF image
    with Image.open(input_path) as img:
        # Save the image in PNG format
        img.save(output_path, 'PNG')
 
# Example usage
convert_tiff_to_png('path/to/your/input_image.tif', 'path/to/your/output_image.png')



#from tensorflow.keras.models import load_model
model = load_model("C:/Users/IsRa.ChaaBani/Desktop/application_brain_tumor_detection/brain-tumor-detection-back/myapi/models/model_cnn_1.h5")

def make_prediction(img):
    images = []
    req = urlopen(img)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1) # 'Load it as it is'
    convert_tiff_to_png
    
    
    img=Image.fromarray(image)
    img=img.resize((224,224))
    img=np.array(img)
    input_img = np.expand_dims(img, axis=0)
    
    res = model.predict(input_img)
    if res:
        print("Tumor Detected")
    else:
        print("No Tumor ")


"""def model_loading(image):
    np_array = np.array(image)
    print(np_array.shape)
    model = load_model('C:/Users/IsRa.ChaaBani/Desktop/application_brain_tumor_detection/brain-tumor-detection-back/myapi/models/model_cnn_1.h5')
    output = model.predict(np_array)
    return output
    """