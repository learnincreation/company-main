# Generated by Django 3.0.7 on 2020-10-14 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_auto_20201014_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drmasterlist',
            name='brand_promotion_plan',
        ),
        migrations.RemoveField(
            model_name='drmasterlist',
            name='current_business',
        ),
        migrations.RemoveField(
            model_name='drmasterlist',
            name='current_prescribing_brand',
        ),
        migrations.RemoveField(
            model_name='drmasterlist',
            name='date',
        ),
        migrations.RemoveField(
            model_name='drmasterlist',
            name='month',
        ),
    ]
