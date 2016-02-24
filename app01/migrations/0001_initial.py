# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u7ec4\u540d\u5b57')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='\u4e3b\u673a\u7ec4\u63cf\u8ff0', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ec4',
                'verbose_name_plural': '\u4e3b\u673a\u7ec4',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='\u4e3b\u673a\u63cf\u8ff0', blank=True)),
                ('ip', models.IPAddressField(verbose_name='\u4e3b\u673aIP\u5730\u5740')),
                ('nationality', models.CharField(max_length=50, null=True, verbose_name='\u4e3b\u673a\u6240\u5c5e\u56fd\u5bb6', blank=True)),
                ('province', models.CharField(max_length=50, null=True, verbose_name='\u4e3b\u673a\u6240\u5c5e\u7701\u4efd', blank=True)),
                ('city', models.CharField(max_length=50, null=True, verbose_name='\u4e3b\u673a\u6240\u5c5e\u57ce\u5e02', blank=True)),
                ('idc', models.CharField(max_length=50, null=True, verbose_name='\u4e3b\u673a\u6240\u5c5e\u673a\u623f', blank=True)),
                ('flood', models.CharField(max_length=50, null=True, verbose_name='\u4e3b\u673a\u6240\u5c5e\u697c\u5c42', blank=True)),
                ('equipment', models.CharField(max_length=50, null=True, verbose_name='\u4e3b\u673a\u6240\u5c5e\u673a\u67dc', blank=True)),
                ('pull_interval', models.IntegerField(max_length=50, verbose_name='\u66f4\u65b0\u65f6\u95f4\u95f4\u9694')),
                ('group', models.ManyToManyField(to='app01.Group', max_length=50, verbose_name='\u4e3b\u673a\u6240\u5c5e\u7ec4')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u540d',
                'verbose_name_plural': '\u4e3b\u673a\u540d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u4efb\u52a1\u540d\u79f0')),
                ('description', models.CharField(max_length=300, verbose_name='\u4efb\u52a1\u63cf\u8ff0')),
                ('task_type', models.CharField(max_length=40, verbose_name='\u4efb\u52a1\u7c7b\u578b', choices=[(b'cmd', b'\xe5\x91\xbd\xe4\xbb\xa4\xe6\x89\xa7\xe8\xa1\x8c'), (b'file_transfer', b'\xe6\x96\x87\xe4\xbb\xb6\xe7\xae\xa1\xe7\x90\x86'), (b'config_manager', b'\xe9\x85\x8d\xe7\xbd\xae\xe7\xae\xa1\xe7\x90\x86')])),
                ('content', models.CharField(max_length=30, verbose_name='\u4efb\u52a1\u5185\u5bb9')),
                ('kick_off_at', models.DateTimeField(null=True, verbose_name='\u4efb\u52a1\u6267\u884c\u65f6\u95f4', blank=True)),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u540d',
                'verbose_name_plural': '\u4efb\u52a1\u540d',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result_type', models.CharField(max_length=40, verbose_name='\u7ed3\u679c\u7c7b\u578b', choices=[(b'success', b'\xe6\x88\x90\xe5\x8a\x9f'), (b'failed', b'\xe5\xa4\xb1\xe8\xb4\xa5'), (b'unknow', b'\xe6\x9c\xaa\xe7\x9f\xa5')])),
                ('result_log', models.TextField(verbose_name='\u7ed3\u679c\u65e5\u5fd7')),
                ('client_info', models.TextField(verbose_name='\u5ba2\u6237\u7aef\u4fe1\u606f')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='\u65e5\u5fd7\u4ea7\u751f\u7684\u65e5\u671f')),
                ('task', models.ForeignKey(verbose_name='\u4efb\u52a1\u65e5\u5fd7', to='app01.TaskCenter')),
            ],
            options={
                'verbose_name': '\u4efb\u52a1\u65e5\u5fd7',
                'verbose_name_plural': '\u4efb\u52a1\u65e5\u5fd7',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('user', models.OneToOneField(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='created_by',
            field=models.ForeignKey(verbose_name='\u4efb\u52a1\u521b\u5efa\u8005', blank=True, to='app01.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='group',
            field=models.ManyToManyField(to='app01.Group', max_length=30, verbose_name='\u4efb\u52a1\u4e3b\u673a\u7ec4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='taskcenter',
            name='host',
            field=models.ManyToManyField(to='app01.Host', max_length=30, verbose_name='\u4efb\u52a1\u4e3b\u673a'),
            preserve_default=True,
        ),
    ]
