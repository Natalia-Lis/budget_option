# Generated by Django 3.0.7 on 2020-06-20 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0002_paymentday_value_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentday',
            name='value_of',
            field=models.FloatField(default=0),
        ),
    ]
