# Generated by Django 3.2.8 on 2021-10-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
