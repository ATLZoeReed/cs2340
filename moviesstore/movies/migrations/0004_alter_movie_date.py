# Generated by Django 5.1.5 on 2025-02-15 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
