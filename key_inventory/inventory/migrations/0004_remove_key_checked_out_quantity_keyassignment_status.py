# Generated by Django 5.0 on 2024-11-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_users_options_keyassignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='checked_out_quantity',
        ),
        migrations.AddField(
            model_name='keyassignment',
            name='status',
            field=models.CharField(choices=[('checked_out', 'Checked Out'), ('returned', 'Returned'), ('lost', 'Lost')], default='checked_out', max_length=20),
        ),
    ]