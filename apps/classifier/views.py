from django.shortcuts import render
from .models import imageDog
from .forms import imageDogForm

# Create your views here.
def index(request):
    form = imageDogForm(request.POST, request.FILES)

    print("test")

    if form.is_valid():
        image = request.FILES['image']
        print(image)
    
    context = {
        'form' : form,
    }

    return render(request, 'index.html', context)