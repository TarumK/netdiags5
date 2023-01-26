# Generated by Django 4.1.5 on 2023-01-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnetdiags', '0004_log_log_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-log_date']},
        ),
        migrations.AddField(
            model_name='log',
            name='log_average',
            field=models.FloatField(default=0.0),
        ),
    ]