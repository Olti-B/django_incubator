# Generated by Django 2.0.7 on 2018-09-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmesRegistraton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=25)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
