# Generated by Django 5.0.2 on 2024-02-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_validationwithtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='validationwithtime',
            name='shown_time',
            field=models.BigIntegerField(default=123),
            preserve_default=False,
        ),
    ]
