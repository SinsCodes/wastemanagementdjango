# Generated by Django 3.2.9 on 2021-12-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20211201_0720'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Phone', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
