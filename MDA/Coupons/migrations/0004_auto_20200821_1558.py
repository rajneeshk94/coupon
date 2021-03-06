# Generated by Django 3.1 on 2020-08-21 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coupons', '0003_auto_20200821_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_SU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10, null=True)),
                ('category', models.CharField(choices=[('Admin', 'Admin'), ('Member', 'Member')], max_length=100, null=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('valid_from', models.DateField(default=datetime.date.today)),
                ('valid_till', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='couponadmin',
            name='code',
            field=models.CharField(default='QWEZZJI3', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='referralformember',
            name='code',
            field=models.CharField(default='YY8RDS', max_length=6, unique=True),
        ),
    ]
