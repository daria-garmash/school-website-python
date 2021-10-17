# Generated by Django 3.2 on 2021-05-21 15:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210423_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Мария', max_length=30, verbose_name='first name')),
                ('father_name', models.CharField(max_length=30, null=True, verbose_name='father name')),
                ('last_name', models.CharField(default='Иванова', max_length=30, verbose_name='last name')),
                ('address', models.TextField(default='address', max_length=100, verbose_name='address')),
                ('birth_date', models.DateField(default='1970-01-01', verbose_name='birth date')),
                ('tel', models.CharField(max_length=10, unique=True, verbose_name='tel')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('position', models.TextField(default='учитель', max_length=50, verbose_name='position')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=30, null=True, verbose_name='father name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='Иванова', max_length=30, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tel',
            field=models.CharField(max_length=10, unique=True, verbose_name='tel'),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='event', max_length=50, verbose_name='event name')),
                ('date', models.DateTimeField(default=datetime.datetime(2021, 5, 21, 18, 52, 2, 844295))),
                ('description', models.TextField(default='this is a description', max_length=500, verbose_name='description')),
                ('responsibleStaff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.schoolstaff')),
            ],
        ),
    ]
