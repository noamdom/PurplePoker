# Generated by Django 3.0.8 on 2020-07-13 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypoker', '0005_auto_20200713_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplemeeting',
            name='ahon',
        ),
        migrations.RemoveField(
            model_name='simplemeeting',
            name='dror',
        ),
        migrations.RemoveField(
            model_name='simplemeeting',
            name='johnny',
        ),
        migrations.RemoveField(
            model_name='simplemeeting',
            name='moshe',
        ),
        migrations.RemoveField(
            model_name='simplemeeting',
            name='noam',
        ),
    ]
