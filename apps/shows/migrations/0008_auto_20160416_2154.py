# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 21:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('shows', '0007_auto_20160416_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowEpisodePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Show Episode',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='showindexpage',
            options={'verbose_name': 'Show Listings'},
        ),
        migrations.AlterModelOptions(
            name='showpage',
            options={'verbose_name': 'Show'},
        ),
        migrations.AddField(
            model_name='showepisodepage',
            name='show',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='episodes', to='shows.ShowPage'),
        ),
    ]
