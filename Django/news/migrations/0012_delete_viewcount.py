# Generated by Django 4.0.1 on 2022-02-17 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_viewcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ViewCount',
        ),
    ]
