# Generated by Django 4.1.5 on 2023-03-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakib', '0002_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider/'),
        ),
    ]