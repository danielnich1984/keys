# Generated by Django 5.0 on 2024-11-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='lname',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]