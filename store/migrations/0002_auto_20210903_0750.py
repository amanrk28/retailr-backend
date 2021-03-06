# Generated by Django 3.2.7 on 2021-09-03 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='cart_product', to='store.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='authentication.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Fruits & Vegetables', 'Fruits And Vegetables'), ('Foodgrains, Oil & Masala', 'Foodgrains Oil Masala'), ('Dairy', 'Dairy'), ('beverages', 'Beverages'), ('Cleaning & Household', 'Cleaning And Household'), ('Beauty & Hygiene', 'Beauty And Hygiene'), ('Snacks', 'Snacks'), ('New', 'New')], default='New', max_length=64),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
