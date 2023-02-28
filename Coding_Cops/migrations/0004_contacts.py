# Generated by Django 4.1.6 on 2023-02-09 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0003_alter_courses_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'ordering': ['email'],
            },
        ),
    ]