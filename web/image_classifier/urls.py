from django.urls import path
from . import views

app_name = "image_classifier"

urlpatterns = [
        path('upload_image', views.uploaded_image, name='upload_image')
]

