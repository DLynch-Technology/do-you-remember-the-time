# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_goals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='goals',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
