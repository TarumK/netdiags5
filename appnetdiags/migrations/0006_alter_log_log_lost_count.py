# Generated by Django 4.1.5 on 2023-01-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnetdiags', '0005_alter_log_options_log_log_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log_lost_count',
            field=models.IntegerField(default=0.0),
        ),
    ]
