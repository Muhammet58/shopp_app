# Generated by Django 4.2.3 on 2023-10-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_usermodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='profilr_photo',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
