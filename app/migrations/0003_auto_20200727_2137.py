# Generated by Django 3.0.7 on 2020-07-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_idea_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='tags',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
    ]