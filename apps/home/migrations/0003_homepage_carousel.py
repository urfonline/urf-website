# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 16:22
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='carousel',
            field=wagtail.wagtailcore.fields.StreamField((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('quotation', wagtail.wagtailcore.blocks.StructBlock((('text', wagtail.wagtailcore.blocks.TextBlock()), ('author', wagtail.wagtailcore.blocks.CharBlock()))))), default=[]),
            preserve_default=False,
        ),
    ]
