# Generated by Django 2.1.5 on 2021-02-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20210218_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='motto',
            field=models.TextField(max_length=24),
        ),
    ]
