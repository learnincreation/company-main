# Generated by Django 3.0.7 on 2020-10-13 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('report', '0002_leavehr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dr_Visit',
            new_name='DrMasterList',
        ),
    ]
