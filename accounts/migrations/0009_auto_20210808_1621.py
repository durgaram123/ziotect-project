# Generated by Django 2.1.5 on 2021-08-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210808_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='title',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]