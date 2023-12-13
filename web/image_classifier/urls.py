from django.urls import path, include
from . import views

app_name = "image_classifier"

urlpatterns = [
        path('success', views.success, name='success'),
        path('upload_image', views.uploaded_image, name='upload_image')
]

