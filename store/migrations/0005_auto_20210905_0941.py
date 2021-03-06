# Generated by Django 3.2.7 on 2021-09-05 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruits & Vegetables', 'Fruits And Vegetables'), ('Foodgrains, Oil & Masala', 'Foodgrains Oil Masala'), ('Dairy', 'Dairy'), ('Beverages', 'Beverages'), ('Cleaning & Household', 'Cleaning And Household'), ('Beauty & Hygiene', 'Beauty And Hygiene'), ('Snacks', 'Snacks'), ('New', 'New')], default='New', max_length=64),
        ),
    ]
