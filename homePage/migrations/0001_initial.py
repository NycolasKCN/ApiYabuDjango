# Generated by Django 4.1.3 on 2022-11-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga_name', models.CharField(max_length=25)),
                ('frontc_over', models.ImageField(upload_to='mangasFrontCover')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=12)),
                ('fav_mangas', models.ManyToManyField(to='homePage.manga')),
            ],
        ),
    ]