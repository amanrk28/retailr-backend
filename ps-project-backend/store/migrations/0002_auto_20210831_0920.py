# Generated by Django 3.2.6 on 2021-08-31 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='image',
            field=models.URLField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
    ]
