# Generated by Django 3.2.9 on 2021-12-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20211222_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo_reg',
            name='images',
            field=models.FileField(default='null', max_length=1000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ngo_reg',
            name='info',
            field=models.FileField(default='null', max_length=1000, upload_to=''),
        ),
    ]
