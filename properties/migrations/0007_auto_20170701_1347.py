# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 13:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='property',
            new_name='property_instance',
        ),
    ]