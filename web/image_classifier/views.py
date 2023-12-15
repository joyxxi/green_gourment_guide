from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .classification_model import image_classify
import logging
logger = logging.getLogger(__name__)


def uploaded_image(request):
    """
    This is the view for uploading image.
    """
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
