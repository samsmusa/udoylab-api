# Generated by Django 4.0.2 on 2022-04-14 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_image_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='default',
        ),
    ]
