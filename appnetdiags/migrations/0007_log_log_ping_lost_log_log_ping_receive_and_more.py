# Generated by Django 4.1.5 on 2023-02-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnetdiags', '0006_alter_log_log_lost_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='log_ping_lost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='log',
            name='log_ping_receive',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_ping_count',
            field=models.IntegerField(default=0),
        ),
    ]