# Generated by Django 3.1.3 on 2021-01-05 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210105_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_confirmed',
            new_name='email_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='email_key',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
