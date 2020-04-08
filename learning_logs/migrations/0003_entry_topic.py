# Generated by Django 3.0.5 on 2020-04-07 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(default=313, on_delete=django.db.models.deletion.PROTECT, to='learning_logs.Topic'),
            preserve_default=False,
        ),
    ]