# Generated by Django 2.1.5 on 2021-08-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210809_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('title1', models.CharField(max_length=255, null=True)),
                ('body1', models.TextField(null=True)),
                ('image1', models.ImageField(null=True, upload_to='images/')),
                ('title2', models.CharField(max_length=255, null=True)),
                ('body2', models.TextField(null=True)),
                ('image2', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
