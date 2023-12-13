from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .classification_model import image_classify
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def uploaded_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            image_path = image_instance.image.path
            predicted_label = image_classify(image_path)
            return redirect('recipes:result', label=predicted_label)
    else:
        form = ImageUploadForm()

    return render(request, 'image_classifier/upload.html', {'form': form})


def success(request):
    return render(request, 'image_classifier/upload_success.html')