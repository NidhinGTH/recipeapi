# Generated by Django 5.0.2 on 2024-03-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipieapp', '0002_alter_recipe_cuisine_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]