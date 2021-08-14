# Generated by Django 2.1.5 on 2021-08-09 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210809_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body1',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body2',
        ),
        migrations.RemoveField(
            model_name='news',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='news',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title2',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='body1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='body2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='image1',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='image2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='text1',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='text2',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='title1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='title2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]