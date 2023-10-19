# Generated by Django 4.0 on 2022-10-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_images_delete_multimedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft'), ('AR', 'Archive')], default='PU', max_length=2),
        ),
    ]
