# Generated by Django 2.1.5 on 2019-01-27 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190127_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
