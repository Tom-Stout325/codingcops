# Generated by Django 4.1.6 on 2023-02-10 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0007_remove_tags_tag_course_remove_tags_tag_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technologies',
            name='tech_image',
            field=models.ImageField(blank=True, default='images/user-default.png', null=True, upload_to='images/'),
        ),
    ]
