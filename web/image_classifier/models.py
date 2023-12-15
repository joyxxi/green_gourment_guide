from django.db import models


class UploadedImage(models.Model):
    # Automatically saved in media/images/
    image = models.ImageField(upload_to="uploaded_images/")
    