from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Holl(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('HollsVid:detailHoll',args=[str(self.pk)])


class video(models.Model):
    title = models.CharField( max_length=50)
    url = models.URLField()
    youtube_id = models.CharField(max_length=50)
    holl = models.ForeignKey('Holl',on_delete=models.CASCADE)
    def __str__(self):
        return self.title