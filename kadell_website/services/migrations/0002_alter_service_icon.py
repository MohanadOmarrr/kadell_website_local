# Generated by Django 4.1 on 2022-08-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(upload_to='images/'),
        ),
    ]