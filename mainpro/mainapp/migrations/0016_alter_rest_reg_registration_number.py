# Generated by Django 3.2.9 on 2021-12-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20211228_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest_reg',
            name='registration_number',
            field=models.CharField(max_length=100),
        ),
    ]