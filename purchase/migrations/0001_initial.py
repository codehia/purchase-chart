# Generated by Django 3.1.4 on 2020-12-06 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('open', 'Open'), ('verified', 'Verified'), ('dispatched', 'Dispatched'), ('delivered', 'Delivered')], max_length=25)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.purchasemodel')),
            ],
        ),
    ]
