# Generated by Django 5.0 on 2024-11-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_keyassignment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='key',
            name='notes',
            field=models.CharField(default=0, max_length=255),
        ),
    ]