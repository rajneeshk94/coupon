# Generated by Django 3.1 on 2020-08-21 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponadmin',
            name='code',
            field=models.CharField(default='567X57EN', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='referralformember',
            name='code',
            field=models.CharField(default='HPUCH9', max_length=6, unique=True),
        ),
    ]