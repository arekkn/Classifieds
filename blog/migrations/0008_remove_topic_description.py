# Generated by Django 4.1.4 on 2023-01-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='description',
        ),
    ]
