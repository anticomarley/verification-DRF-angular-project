# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-30 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('everify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatesubmittionhistory',
            name='submittion_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userdocuments',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='verifiedcertificates',
            name='verified_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]