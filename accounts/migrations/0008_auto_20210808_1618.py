# Generated by Django 2.1.5 on 2021-08-08 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210808_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribe',
            name='email',
        ),
        migrations.AddField(
            model_name='subscribe',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
