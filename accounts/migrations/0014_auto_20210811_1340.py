# Generated by Django 2.1.5 on 2021-08-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_top'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='top',
            name='image',
        ),
        migrations.RemoveField(
            model_name='top',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='top',
            name='image2',
        ),
    ]