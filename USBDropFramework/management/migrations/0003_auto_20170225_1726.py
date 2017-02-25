# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_datapoint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='target',
            old_name='target_name',
            new_name='name',
        ),
    ]
