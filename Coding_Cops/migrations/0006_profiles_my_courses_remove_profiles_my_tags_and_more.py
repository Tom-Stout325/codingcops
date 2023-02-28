# Generated by Django 4.1.6 on 2023-02-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0005_profiles_my_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='my_courses',
            field=models.ManyToManyField(blank=True, null=True, to='Coding_Cops.courses'),
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='my_tags',
        ),
        migrations.AddField(
            model_name='profiles',
            name='my_tags',
            field=models.ManyToManyField(blank=True, max_length=100, null=True, to='Coding_Cops.tags'),
        ),
    ]
