# Generated by Django 3.0.5 on 2020-04-11 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20200411_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='date_added',
            new_name='data_added',
        ),
    ]
