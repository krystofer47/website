# Generated by Django 3.1.1 on 2020-09-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20200918_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='post.Tag'),
        ),
    ]
