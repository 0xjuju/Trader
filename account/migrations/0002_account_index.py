# Generated by Django 4.1.7 on 2023-03-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
