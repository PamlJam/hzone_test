# Generated by Django 2.1.5 on 2021-02-18 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20210215_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='browse',
            field=models.IntegerField(default=0),
        ),
    ]
