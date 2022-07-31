# Generated by Django 4.0.6 on 2022-07-30 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0005_third_party'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('status', models.CharField(max_length=12)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallets.customer')),
            ],
        ),
    ]
