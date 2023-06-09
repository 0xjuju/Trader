# Generated by Django 4.1.7 on 2023-03-28 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_index_account_account_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='account_index',
        ),
        migrations.AddField(
            model_name='account',
            name='index',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(default='', max_length=42, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='private_key',
            field=models.CharField(default='', max_length=66, unique=True),
        ),
    ]
