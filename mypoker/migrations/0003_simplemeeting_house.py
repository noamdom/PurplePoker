# Generated by Django 3.0.8 on 2020-07-13 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypoker', '0002_player1'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplemeeting',
            name='house',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mypoker.Player1'),
        ),
    ]
