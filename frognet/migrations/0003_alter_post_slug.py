# Generated by Django 5.1.4 on 2025-01-04 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frognet', '0002_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
    ]
