from django.shortcuts import render
from .forms import imageDogForm
from fastbook import *
from fastai.vision.all import *
from base64 import b64encode
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
BASE_DIR = Path(__file__).resolve().parent.parent
filepath = os.path.join(BASE_DIR, 'classifier/model.pkl')
model = load_learner(filepath)
classes = model.dls.vocab

def classify(img_file):
    img = PILImage.create(img_file[0])
    prediction = model.predict(img)
    probs_list = prediction[2].numpy()
    encoded = b64encode(img_file[1])
    encoded = encoded.decode('ascii')
    mime = "image/jpg"
    image_uri = "data:%s;base64,%s" % (mime, encoded)
    return {
        'image' : image_uri,
        'category': classes[prediction[1].item()],
        'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
    }

# Create your views here.
def index(request):
    form = imageDogForm(request.POST, request.FILES)
    result = {}
    #print(result)

    if form.is_valid():
        image = [request.FILES['image'], form.cleaned_data['image'].file.read()]
        result = classify(image)
    
    context = {
        'form' : form,
        'result' : result,
    }

    return render(request, 'index.html', context)