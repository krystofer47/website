# Generated by Django 3.1.1 on 2020-09-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200918_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
