# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20170701_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=80, null=True)),
                ('image', models.ImageField(upload_to='properties/rooms/')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='properties.Property')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'verbose_name': 'Gallery',
            },
        ),
    ]
