# Generated by Django 3.0.7 on 2020-06-20 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0004_auto_20200619_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='money_max',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='zapasowa',
        ),
    ]
