# Generated by Django 3.2.7 on 2021-09-13 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0003_auto_20210913_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]