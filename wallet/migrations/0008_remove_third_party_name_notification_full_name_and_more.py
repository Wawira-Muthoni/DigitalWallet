# Generated by Django 4.0.6 on 2022-07-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0007_receipt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='third_party',
            name='name',
        ),
        migrations.AddField(
            model_name='notification',
            name='full_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='third_party',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='third_party',
            name='transaction_cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='third_party',
            name='user_id',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
