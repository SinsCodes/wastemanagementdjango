# Generated by Django 3.2.9 on 2021-12-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20211224_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest_reg',
            name='images',
            field=models.CharField(default='null', max_length=200),
        ),
        migrations.AddField(
            model_name='rest_reg',
            name='info',
            field=models.CharField(default='null', max_length=200),
        ),
    ]