from django.db import models

# Create your models here.
class imageDog(models.Model):
    image = models.ImageField()