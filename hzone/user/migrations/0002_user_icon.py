# Generated by Django 2.1.5 on 2021-02-14 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
