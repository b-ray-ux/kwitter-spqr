# Generated by Django 2.2 on 2021-06-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kwitter_app', '0003_auto_20210612_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='document/%Y/%m/%d'),
        ),
    ]
