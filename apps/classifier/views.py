from django.shortcuts import render
from .models import imageDog
from .forms import imageDogForm
from fastbook import *
from fastai.vision.all import *
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
BASE_DIR = Path(__file__).resolve().parent.parent
filepath = os.path.join(BASE_DIR, 'classifier/model.pkl')
model = load_learner(filepath)
classes = model.dls.vocab

def classify(img_file):
    img = PILImage.create(img_file)
    prediction = model.predict(img)
    probs_list = prediction[2].numpy()
    #print(classes[prediction[1].item()])
    #print({round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)})
    return {
        'category': classes[prediction[1].item()],
        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
    }

# Create your views here.
def index(request):
    form = imageDogForm(request.POST, request.FILES)
    result = {}
    #print(result)

    if form.is_valid():
        image = request.FILES['image']
        result = classify(image)
    
    context = {
        'form' : form,
        'result' : result,
    }

    return render(request, 'index.html', context)