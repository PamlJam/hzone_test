# Generated by Django 2.1.5 on 2021-02-18 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_user_browse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='motto',
            field=models.TextField(default='这个人很懒的啦，什么也没写', max_length=24),
        ),
    ]
