# Generated by Django 2.1.5 on 2019-01-28 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190127_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
