# Generated by Django 3.1.5 on 2021-01-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
