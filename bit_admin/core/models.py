# coding: utf-8
from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
from django.utils.timezone import get_current_timezone


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class News(BaseModel):
    source_choices = (
        (1, '财联社'),
        (2, '财新网'),
    )
    title = models.TextField()
    link = models.CharField(max_length=512)
    source = models.IntegerField(default=1, choices=source_choices)
    hash = models.CharField(max_length=64, unique=True)
    sid = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return '{0}'.format(self.title)

    def __repr__(self):
        return '{0}'.format(self.title)
