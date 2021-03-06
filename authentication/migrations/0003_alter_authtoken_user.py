# Generated by Django 3.2.7 on 2021-09-05 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210902_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_tokens', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
