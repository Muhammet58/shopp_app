# Generated by Django 4.2.3 on 2023-10-22 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopp_app', '0008_remove_mybasket_model_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybasket_model',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopp_app.shopping_model'),
        ),
        migrations.AlterField(
            model_name='myfavorite_model',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopp_app.shopping_model'),
        ),
    ]