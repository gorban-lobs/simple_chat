# Generated by Django 2.2.5 on 2019-09-05 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_is_red'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_date',
            new_name='sended_time',
        ),
    ]