from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.getData),
    path('make_prediction/', views.make_prediction)
]