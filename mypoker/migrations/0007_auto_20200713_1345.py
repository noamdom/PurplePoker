# Generated by Django 3.0.8 on 2020-07-13 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mypoker', '0006_auto_20200713_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplegame',
            name='meeting',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='mypoker.simpleMeeting'),
        ),
    ]