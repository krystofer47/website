# Generated by Django 3.1.1 on 2020-09-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exposee',
            field=models.CharField(default='Eine atemberaubende Geshichte über einen Riesen der eines Tages nicht mehr weiß wie groß er ist', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]