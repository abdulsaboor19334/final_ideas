# Generated by Django 3.1.5 on 2021-01-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210111_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
