# Generated by Django 2.0.7 on 2018-10-07 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0007_auto_20181007_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmesregistraton',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 15, 25, 32, 407439, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 15, 25, 32, 408455, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='soldproduct',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 15, 25, 32, 408455, tzinfo=utc)),
        ),
    ]
