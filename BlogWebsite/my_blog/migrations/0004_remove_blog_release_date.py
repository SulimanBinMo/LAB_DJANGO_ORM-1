# Generated by Django 4.2 on 2023-05-29 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0003_alter_blog_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='release_date',
        ),
    ]