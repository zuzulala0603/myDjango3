# Generated by Django 3.0.6 on 2020-11-27 12:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notice',
            new_name='Post',
        ),
    ]
