# Generated by Django 4.1.6 on 2023-02-07 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('link', models.URLField(max_length=300)),
                ('tech_image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(default='', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Tech',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(blank=True, default='images/user-default.png', null=True, upload_to='images/')),
                ('private', models.BooleanField(default=False)),
                ('goals', models.TextField(default='Workin on it,  Please check back!')),
                ('bio', models.TextField(default='Workin on it, Please check back!')),
                ('social_github', models.URLField(blank=True, max_length=300, null=True)),
                ('social_linkedin', models.URLField(blank=True, max_length=300, null=True)),
                ('social_website', models.URLField(blank=True, max_length=300, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, default='', null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'ordering': ['slug'],
            },
        ),
    ]
