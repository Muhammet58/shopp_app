# Generated by Django 4.2.3 on 2023-10-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_usermodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='phone_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]