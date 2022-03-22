from operator import mod
from django.db import models
from matplotlib import image
from matplotlib.pyplot import text

class Post(models.Model):
    title = models.CharField(max_length=300)
    data = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='event_image/')
