# Generated by Django 4.1.6 on 2023-02-08 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralSystem', '0027_alter_vehicle_color_alter_vehicle_vehicle'),
        ('BOX_SMART', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosapi',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GeneralSystem.device'),
        ),
        migrations.AlterField(
            model_name='dadosapi',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
