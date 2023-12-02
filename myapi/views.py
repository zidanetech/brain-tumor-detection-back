from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import application
import cv2
import random

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
    # print(request.data.get('img'))
    image = application.make_prediction(request.data.get('img')) # get image's matrix
    print(image)