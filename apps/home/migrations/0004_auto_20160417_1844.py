# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('copy', models.TextField()),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='carousel',
        ),
        migrations.AddField(
            model_name='homepageslider',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='home.HomePage'),
        ),
    ]