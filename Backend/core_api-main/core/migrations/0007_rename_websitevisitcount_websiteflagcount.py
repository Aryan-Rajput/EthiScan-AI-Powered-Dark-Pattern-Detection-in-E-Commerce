# Generated by Django 4.1 on 2024-01-08 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_category_patternname_websitevisitcount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WebsiteVisitCount',
            new_name='websiteFlagCount',
        ),
    ]
