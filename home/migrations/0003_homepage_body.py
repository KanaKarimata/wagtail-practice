# Generated by Django 5.0.4 on 2024-04-29 03:26

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
