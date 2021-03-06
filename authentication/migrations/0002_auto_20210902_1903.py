# Generated by Django 3.2.7 on 2021-09-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authtoken',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='authtoken',
            name='deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='authtoken',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
