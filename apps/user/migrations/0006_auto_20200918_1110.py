# Generated by Django 3.1.1 on 2020-09-18 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200918_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='favorite_color',
            new_name='favourite_color',
        ),
    ]
