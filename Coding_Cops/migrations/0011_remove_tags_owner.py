# Generated by Django 4.1.6 on 2023-02-10 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0010_remove_profiles_my_courses_remove_profiles_my_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='owner',
        ),
    ]
