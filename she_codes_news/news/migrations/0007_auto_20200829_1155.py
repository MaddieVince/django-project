# Generated by Django 3.0.8 on 2020-08-29 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200829_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
