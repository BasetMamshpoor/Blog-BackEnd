# Generated by Django 4.0 on 2022-08-16 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='owner',
        ),
    ]
