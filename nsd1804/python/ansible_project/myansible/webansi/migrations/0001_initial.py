# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-19 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnsibleModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True)),
                ('ipaddr', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModuleArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arg_text', models.CharField(max_length=100)),
                ('mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webansi.AnsibleModule')),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='hostgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webansi.HostGroup'),
        ),
    ]