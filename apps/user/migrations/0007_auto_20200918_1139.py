# Generated by Django 3.1.1 on 2020-09-18 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200918_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='last_edited',
            new_name='modified',
        ),
    ]