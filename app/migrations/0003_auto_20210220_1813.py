# Generated by Django 3.1.6 on 2021-02-20 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210220_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='upload',
            field=models.FileField(default=True, upload_to='media'),
        ),
    ]
