# Generated by Django 2.0.7 on 2018-10-07 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0006_auto_20181007_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmesregistraton',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 15, 18, 15, 650822, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 15, 18, 15, 651861, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='soldproduct',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 15, 18, 15, 651861, tzinfo=utc)),
        ),
    ]