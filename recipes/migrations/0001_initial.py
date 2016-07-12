# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ingredients', models.CharField(max_length=500)),
                ('body_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('instructions', models.CharField(max_length=1000)),
                ('body_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('cuisine', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date added')),
                ('mod_date', models.DateTimeField(verbose_name='last modified')),
            ],
        ),
        migrations.AddField(
            model_name='instructions',
            name='recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(to='recipes.Recipe'),
        ),
    ]
