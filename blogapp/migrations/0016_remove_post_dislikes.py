# Generated by Django 3.2.16 on 2023-02-17 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0015_post_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
    ]
