# Generated by Django 4.0.2 on 2022-04-16 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_imagealbum_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]
