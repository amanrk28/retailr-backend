# Generated by Django 3.2.7 on 2021-09-06 09:58

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0005_auto_20210905_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('dispatched', 'Dispatched'), ('closed', 'Closed')], default='new', max_length=20)),
                ('hash', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('delivery_address', models.JSONField(default=authentication.models.get_address)),
                ('delivery_date', models.DateTimeField(blank=True, null=True)),
                ('expected_delivery_date', models.DateTimeField(blank=True, null=True)),
                ('dispatch_date', models.DateTimeField(blank=True, null=True)),
                ('expected_dispatch_date', models.DateTimeField(blank=True, null=True)),
                ('closed', models.BooleanField(default=False)),
                ('more_details', models.JSONField(default=order.models.get_more_details)),
                ('placed_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.product')),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
    ]