# Generated by Django 2.1.5 on 2021-02-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20210215_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='icon/default.jpg', upload_to='static/icon'),
        ),
    ]
