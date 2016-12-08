# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_name', models.CharField(max_length=50, verbose_name=b'Article Name')),
                ('article_desc', models.CharField(max_length=500, verbose_name=b'Article Description')),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'Image')),
                ('image_name', models.CharField(max_length=30, verbose_name=b'Image Alt Text')),
            ],
        ),
    ]
