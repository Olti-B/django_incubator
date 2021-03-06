# Generated by Django 2.0.7 on 2018-10-07 12:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0003_auto_20180928_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=225)),
                ('content', models.CharField(max_length=225)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 12, 13, 31, 12843, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='SoldProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 12, 13, 31, 12843, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='farmesregistraton',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 12, 13, 31, 12843, tzinfo=utc)),
        ),
    ]
