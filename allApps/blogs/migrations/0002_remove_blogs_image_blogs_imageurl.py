# Generated by Django 4.1.7 on 2023-02-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='image',
        ),
        migrations.AddField(
            model_name='blogs',
            name='imageUrl',
            field=models.URLField(null=True),
        ),
    ]
