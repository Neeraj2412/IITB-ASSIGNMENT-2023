# Generated by Django 4.1.7 on 2023-02-19 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_blogs_image_blogs_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
