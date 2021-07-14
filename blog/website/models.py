from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()

    imagem = models.ImageField(upload_to='posts', null=True, blank=True)