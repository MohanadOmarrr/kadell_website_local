# Generated by Django 4.1 on 2022-08-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_service_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='body',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
