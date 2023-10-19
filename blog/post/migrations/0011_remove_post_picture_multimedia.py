# Generated by Django 4.0 on 2022-10-02 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.CreateModel(
            name='MultiMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='post_medias')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='post.post')),
            ],
        ),
    ]