# Generated by Django 3.2.7 on 2024-01-01 01:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20231231_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pins',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 2, 1, 25, 49, 604166, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='worldcup',
            name='info',
            field=models.CharField(blank=True, default='No Info Yet', max_length=2000, null=True),
        ),
    ]
