# Generated by Django 4.1.6 on 2023-02-10 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0009_alter_profiles_my_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='my_courses',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='my_tags',
        ),
    ]
