# Generated by Django 4.1.6 on 2023-02-10 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0006_profiles_my_courses_remove_profiles_my_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='tag_course',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tag_profile',
        ),
        migrations.AddField(
            model_name='tags',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Coding_Cops.profiles'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='my_courses',
            field=models.ManyToManyField(to='Coding_Cops.courses'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='my_tags',
            field=models.ManyToManyField(to='Coding_Cops.tags'),
        ),
    ]
