# Generated by Django 3.1.6 on 2023-01-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
