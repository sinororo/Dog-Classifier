from django.shortcuts import render
from .models import imageDog
from .forms import imageDogForm

# Create your views here.
def index(request):
    form = imageDogForm(request.POST or None)

    if form.is_valid():
        print("Image Uploaded")
    
    context = {
        'form' : form,
    }

    return render(request, 'index.html', context)