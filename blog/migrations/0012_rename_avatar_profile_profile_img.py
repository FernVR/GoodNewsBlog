# Generated by Django 4.2.15 on 2024-09-24 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_excerpt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='profile_img',
        ),
    ]
