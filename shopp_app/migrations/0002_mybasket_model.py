# Generated by Django 4.2.3 on 2023-08-16 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myBasket_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopp_app.shopping_model')),
            ],
        ),
    ]
