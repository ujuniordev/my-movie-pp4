# Generated by Django 3.2.18 on 2023-04-18 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0008_remove_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
    ]