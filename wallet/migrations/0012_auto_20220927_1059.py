# Generated by Django 2.2.12 on 2022-09-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0011_auto_20220908_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='card',
            name='issuer',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='currency',
            name='symbol',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='customer',
            name='nationality',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_id',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='full_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='isActive',
            field=models.BooleanField(max_length=15),
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='location',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_code',
            field=models.CharField(max_length=30),
        ),
    ]
