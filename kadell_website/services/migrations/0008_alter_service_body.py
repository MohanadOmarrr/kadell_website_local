# Generated by Django 4.1 on 2022-08-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='body',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
