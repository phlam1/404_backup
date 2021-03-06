# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid
import web_api.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('git', models.CharField(blank=True, max_length=35, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('url', models.URLField()),
                ('friends', models.ManyToManyField(blank=True, related_name='_author_friends_+', to='web_api.Author')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('publish_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('tag', web_api.utils.ListField(blank=True, default=[])),
                ('visibility', models.CharField(choices=[(b'1', b'Public'), (b'2', b'Public to local'), (b'3', b'Friends of friends'), (b'4', b'Local friends'), (b'5', b'friend selected'), (b'6', b'Myself only')], default=b'1', max_length=1)),
                ('publish_time', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Author')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Post'),
        ),
    ]
