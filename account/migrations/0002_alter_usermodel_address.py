# Generated by Django 4.2.3 on 2023-10-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
