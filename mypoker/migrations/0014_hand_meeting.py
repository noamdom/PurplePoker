# Generated by Django 3.0.8 on 2020-07-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypoker', '0013_hand_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='hand',
            name='meeting',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hands', to='mypoker.simpleMeeting'),
        ),
    ]
