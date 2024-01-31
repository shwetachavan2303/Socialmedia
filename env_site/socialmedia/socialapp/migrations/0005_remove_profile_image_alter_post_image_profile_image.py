# Generated by Django 4.2.4 on 2023-09-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0004_alter_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Image',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images'),
        ),
    ]
