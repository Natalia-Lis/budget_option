# Generated by Django 3.0.7 on 2020-06-20 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentday',
            name='value_of',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
