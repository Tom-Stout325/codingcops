# Generated by Django 4.1.6 on 2023-02-10 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Coding_Cops', '0004_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='my_tags',
            field=models.ForeignKey(blank=True, default='', max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='Coding_Cops.tags'),
        ),
    ]
