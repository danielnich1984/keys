# Generated by Django 5.0 on 2024-11-05 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_key_checked_out_quantity_keyassignment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyassignment',
            name='status',
            field=models.CharField(choices=[('CHECKED_OUT', 'Checked Out'), ('LOST', 'Lost')], default='CHECKED_OUT', max_length=15),
        ),
    ]
