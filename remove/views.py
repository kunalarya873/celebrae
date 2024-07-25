# views.py
from django.shortcuts import render
from django.http import FileResponse
from .models import Picture
from rembg import remove
from PIL import Image
import os
from .forms import PictureForm

def index(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            return _extracted_from_index_5(request, form)
    else:
        form = PictureForm()
    return render(request,'index.html', {'form': form})

def _extracted_from_index_5(request, form):
    # Save the form instance to get the uploaded image
    instance = form.save()

    # Get the path of the uploaded image
    input_path = instance.image.path
    rmv(input_path)
    output_path = 'media/outputs/removed.png'

    # Return a file response to trigger the download
    return FileResponse(open(output_path, 'rb'), as_attachment=True, filename='celebrae.png')

def rmv(input_path):
    output_path = 'media/outputs/removed.png'
    
    input_image = Image.open(input_path)
    output = remove(input_image)
    
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    
    output.save(output_path)
