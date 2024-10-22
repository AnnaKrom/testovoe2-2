from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_upload')
    else:
        form = ImageForm()

    images = Image.objects.all()
    return render(request, 'images/upload.html', {'form': form, 'images': images})

def image_view(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    return render(request, 'images/view.html', {'image': image})        

def image_delete(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    return redirect('image_upload')
