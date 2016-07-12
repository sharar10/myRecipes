# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='instructions',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Ingredients',
        ),
        migrations.DeleteModel(
            name='Instructions',
        ),
    ]
