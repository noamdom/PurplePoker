# Generated by Django 3.0.8 on 2020-07-13 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypoker', '0011_auto_20200713_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hand',
            old_name='diet',
            new_name='type',
        ),
    ]
