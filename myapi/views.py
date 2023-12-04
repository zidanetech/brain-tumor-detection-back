import os
from urllib.request import urlopen
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import application
import cv2
import random
from werkzeug.utils import secure_filename
import numpy as np



# Create your views here.


# Get test API
@api_view(['GET'])
def getData(request):
    return Response({
        "message": "Bonjour"
    })



# Post API
# Prediction URL
@api_view(['POST'])
def make_prediction(request):
    f=request.data.get('img')
    req = urlopen(f)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, -1) # 'Load it as it is'
    basepath = os.path.dirname(__file__)
    """file_path = os.path.join(
                basepath, 'image', secure_filename(image.filename))"""
    #f.save(file_path)
    cv2.imwrite("nom_fichier.tif", image)
    value= application.getResult("nom_fichier.tif")
    result= application.get_className(value)
    print(result)
    return Response({
        "message": result
    })
