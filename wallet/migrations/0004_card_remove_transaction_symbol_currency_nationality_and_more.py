# Generated by Django 4.0.6 on 2022-07-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_transaction_symbol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=8)),
                ('expiry_date', models.DateTimeField()),
                ('card_type', models.CharField(max_length=6)),
                ('date_issued', models.DateTimeField()),
                ('issuer', models.CharField(max_length=6)),
                ('secuity_code', models.SmallIntegerField()),
                ('signature', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='symbol',
        ),
        migrations.AddField(
            model_name='currency',
            name='nationality',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
