# Generated by Django 3.0.7 on 2020-06-22 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0006_auto_20200622_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('credit_amount', models.FloatField()),
                ('should_end_on', models.DateField(null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collected_money', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RepaymentDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repayment_date', models.DateField(auto_now_add=True)),
                ('repayment_value', models.FloatField(default=0)),
                ('repayment_collected', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget_app.Repayment')),
                ('repayment_credits', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget_app.Credits')),
            ],
        ),
        migrations.AddField(
            model_name='repayment',
            name='payment_target',
            field=models.ManyToManyField(through='budget_app.RepaymentDay', to='budget_app.Credits'),
        ),
    ]