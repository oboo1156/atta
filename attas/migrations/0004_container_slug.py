# Generated by Django 3.2.8 on 2021-10-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attas', '0003_alter_container_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique_for_date='date'),
        ),
    ]
