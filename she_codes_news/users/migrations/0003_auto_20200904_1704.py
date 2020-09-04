# Generated by Django 3.0.8 on 2020-09-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200901_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_author',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
