# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150804_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='utensils',
            field=models.TextField(null=True),
        ),
    ]
