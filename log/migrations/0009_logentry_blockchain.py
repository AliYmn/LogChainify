# Generated by Django 4.1.7 on 2023-04-16 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0008_logentry_secure_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='blockchain',
            field=models.CharField(choices=[('eth', 'Ethereum'), ('btc', 'Bitcoin'), ('doge', 'Dogecoin'), ('ltc', 'Litecoin')], default='eth', max_length=4),
        ),
    ]