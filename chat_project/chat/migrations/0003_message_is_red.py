# Generated by Django 2.2.5 on 2019-09-04 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20190904_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_red',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]