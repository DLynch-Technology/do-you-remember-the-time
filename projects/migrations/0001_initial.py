# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('project_code', models.CharField(max_length=6)),
                ('date_start', models.DateField(null=True, blank=True)),
                ('date_expected', models.DateField(null=True, blank=True)),
                ('date_completion', models.DateField(null=True, blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(related_name='create', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(related_name='modified', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, to='projects.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
