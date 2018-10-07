# Generated by Django 2.0.7 on 2018-10-07 12:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0004_auto_20181007_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='postproduct',
            name='image',
            field=models.ImageField(default='notset', upload_to=''),
        ),
        migrations.AlterField(
            model_name='farmesregistraton',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 12, 18, 48, 406456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 12, 18, 48, 407456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='soldproduct',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 10, 7, 12, 18, 48, 406456, tzinfo=utc)),
        ),
    ]