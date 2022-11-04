from django.urls import path
from . import views

app_name = 'welcomepizza'

urlpatterns = [
    path('', views.index, name="index"), 
]