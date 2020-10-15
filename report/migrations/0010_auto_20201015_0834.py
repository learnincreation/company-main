# Generated by Django 3.0.7 on 2020-10-15 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('report', '0009_monthplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyActivites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_field', models.BooleanField(default=False)),
                ('is_meeting', models.BooleanField(default=False)),
                ('is_workFromHome', models.BooleanField(default=False)),
                ('is_adminDay', models.BooleanField(default=False)),
                ('is_covid19', models.BooleanField(default=False)),
                ('is_other', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.DeleteModel(
            name='MonthPlan',
        ),
    ]