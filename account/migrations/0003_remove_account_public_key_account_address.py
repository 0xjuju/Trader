# Generated by Django 4.1.7 on 2023-03-28 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='public_key',
        ),
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(default='', max_length=42),
        ),
    ]
