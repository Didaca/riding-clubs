# Generated by Django 4.0.3 on 2022-11-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horsebreed',
            name='breed_photo',
            field=models.ImageField(blank=True, null=True, upload_to='breeds_photo'),
        ),
    ]