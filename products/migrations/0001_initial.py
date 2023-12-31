# Generated by Django 4.2.4 on 2023-08-13 21:16

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.utils.upload_image_path)),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=20)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
