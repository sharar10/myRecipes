# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_utensils'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date modified'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
