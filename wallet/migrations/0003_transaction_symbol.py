# Generated by Django 4.0.6 on 2022-07-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_account_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='symbol',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
