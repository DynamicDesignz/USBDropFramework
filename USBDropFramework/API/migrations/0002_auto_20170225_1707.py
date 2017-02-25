# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_datapoint'),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='targetdata',
            name='computer_name',
        ),
        migrations.RemoveField(
            model_name='targetdata',
            name='target_id',
        ),
        migrations.RemoveField(
            model_name='targetdata',
            name='test_id',
        ),
        migrations.AddField(
            model_name='targetdata',
            name='datapoint',
            field=models.ForeignKey(default=None, to='management.DataPoint'),
        ),
        migrations.AddField(
            model_name='targetdata',
            name='target',
            field=models.ForeignKey(default=None, to='management.Target'),
        ),
        migrations.AddField(
            model_name='targetdata',
            name='test',
            field=models.ForeignKey(default=None, to='management.Test'),
        ),
        migrations.AlterField(
            model_name='targetdata',
            name='ip_address',
            field=models.GenericIPAddressField(),
        ),
    ]
