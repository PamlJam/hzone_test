# Generated by Django 2.1.5 on 2021-02-14 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20210215_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='icon/default.jpg', upload_to='icon/'),
        ),
    ]
