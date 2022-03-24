from operator import mod
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    data = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='event_image/')

    def get_summary(self):
        return self.text[:70]

    def __str__(self):
        return self.title