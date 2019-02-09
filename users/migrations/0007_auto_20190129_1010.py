# Generated by Django 2.1.5 on 2019-01-29 16:10

from django.db import migrations, models
import django.utils.crypto


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=8, primary_key=True, serialize=False),
        ),
    ]