# Generated by Django 2.2.6 on 2019-12-03 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190115_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='discord_id',
            field=models.BigIntegerField(null=True, verbose_name='ID do Discord'),
        ),
    ]