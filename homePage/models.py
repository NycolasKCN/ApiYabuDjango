from django.db import models

# Create your models here.

class Manga(models.Model):
    manga_id = models.BigAutoField(primary_key=True)
    manga_name = models.CharField(max_length=25)
    frontc_over = models.ImageField(upload_to="mangasFrontCover")

    def __str__(self) -> str:
        return self.manga_name

    @property
    def manga_id(self):
        return self.manga_id

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=12)
    fav_mangas = models.ManyToManyField(Manga)

    def __str__(self) -> str:
        return self.user_name

    @property
    def user_id(self):
        return self.user_id
