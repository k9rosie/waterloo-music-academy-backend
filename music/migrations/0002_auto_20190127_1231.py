# Generated by Django 2.1.5 on 2019-01-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, height_field=1600, upload_to='album_imgs', width_field=1600),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, height_field=1600, upload_to='artist_imgs', width_field=1600),
        ),
    ]