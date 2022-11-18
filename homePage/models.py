from django.db import models

# Create your models here.

class Manga(models):
    name = models.CharField()
    frontCover = models.ImageField(upload_to="mangaFrontCover")