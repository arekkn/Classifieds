# Generated by Django 4.1.4 on 2023-01-14 22:20

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=31, verbose_name=django.contrib.auth.models.User),
        ),
    ]
