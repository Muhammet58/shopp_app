# Generated by Django 4.2.3 on 2023-10-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_rename_profilr_photo_usermodel_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_photo',
            field=models.ImageField(upload_to='image'),
        ),
    ]
