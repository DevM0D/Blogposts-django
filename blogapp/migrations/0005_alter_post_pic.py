# Generated by Django 3.2.16 on 2023-02-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20230215_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/UserMedia/'),
        ),
    ]