# Generated by Django 3.0.7 on 2020-07-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_idea_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
