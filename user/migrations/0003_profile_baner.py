# Generated by Django 5.1.4 on 2025-01-04 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_options_alter_profile_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='baner',
            field=models.ImageField(default='5.jpg', upload_to='images', verbose_name='Банер профиля'),
        ),
    ]
