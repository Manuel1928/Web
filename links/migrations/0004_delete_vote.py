# Generated by Django 3.1.3 on 2022-10-04 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
