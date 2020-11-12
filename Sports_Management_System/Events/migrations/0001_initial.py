# Generated by Django 3.1 on 2020-11-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
                ('organiser', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
    ]
