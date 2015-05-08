# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestDemographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('age_range', models.CharField(max_length=20, choices=[('< 18', '< 18'), ('18 - 25', '18 - 25'), ('25 - 40', '25 - 40'), ('40+', '40+')])),
                ('music_job', models.CharField(max_length=100, choices=[('< 18', '< 18'), ('18 - 25', '18 - 25'), ('25 - 40', '25 - 40'), ('40+', '40+')])),
                ('music_personal', models.CharField(max_length=100, choices=[('< 18', '< 18'), ('18 - 25', '18 - 25'), ('25 - 40', '25 - 40'), ('40+', '40+')])),
                ('music_experience_pro', models.CharField(max_length=100, choices=[('< 18', '< 18'), ('18 - 25', '18 - 25'), ('25 - 40', '25 - 40'), ('40+', '40+')])),
                ('music_experience_stu', models.CharField(max_length=100, choices=[('< 18', '< 18'), ('18 - 25', '18 - 25'), ('25 - 40', '25 - 40'), ('40+', '40+')])),
                ('music_genres', models.CharField(max_length=100)),
                ('music_event', models.CharField(max_length=100)),
                ('music_last_event', models.CharField(max_length=100)),
                ('like', models.CharField(max_length=100)),
                ('improve', models.CharField(max_length=500)),
                ('other', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestPlay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_skipped', models.BooleanField(default=False)),
                ('is_listened_before', models.BooleanField(default=False)),
                ('listened_ratio', models.IntegerField(default=50)),
                ('skipping_reason', models.CharField(blank=True, max_length=16, null=True, choices=[('NOT_INTERESTING', 'Not interesting or exciting enough'), ('TOO_LONG', 'Interesting but too long or repetitive'), ('NOT_MY_TASTE', 'Just not my taste'), ('NOT_RIGHT_MOOD', 'Not the right mood, but would listen to it again')])),
                ('musaic', models.ForeignKey(to='music_feeder.MusicFile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
                ('ip_address', models.IPAddressField()),
                ('referral_link', models.CharField(max_length=200)),
                ('referral_code', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='testplay',
            name='session',
            field=models.ForeignKey(to='music_feeder.TestSession'),
            preserve_default=True,
        ),
    ]
