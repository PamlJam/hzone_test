# Generated by Django 2.1.5 on 2021-02-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20210215_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='./static/icon/default.jpg', upload_to='./static/icon/'),
        ),
    ]
