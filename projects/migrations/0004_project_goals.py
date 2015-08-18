# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='goals',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
