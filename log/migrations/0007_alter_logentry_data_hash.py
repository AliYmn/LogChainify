# Generated by Django 4.1.7 on 2023-04-16 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_alter_logentry_data_alter_logentry_data_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logentry',
            name='data_hash',
            field=models.CharField(default='Pending...', max_length=100),
        ),
    ]
