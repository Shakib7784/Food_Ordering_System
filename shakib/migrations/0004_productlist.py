# Generated by Django 4.1.5 on 2023-03-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shakib', '0003_alter_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='productList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='product/')),
                ('price', models.FloatField(blank=True, max_length=50)),
            ],
        ),
    ]
