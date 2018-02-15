# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import binascii
import os

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import _user_has_perm, _user_get_all_permissions, _user_has_module_perms


import mongoengine
from mongoengine.django import auth
from mongoengine import fields, Document

class User(Document):

    id = fields.IntField(primary_key=True)
    username = fields.StringField(required=True)
    email = fields.EmailField()
    name = fields.StringField()
    password = fields.StringField(
        max_length=128,
        verbose_name=_('password'),
        help_text=_("Use '[algo]$[iterations]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>.")
    )

    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)
    is_superuser = fields.BooleanField(default=False)

    last_login = fields.DateTimeField(default=timezone.now, verbose_name=_('last login'))
    date_joined = fields.DateTimeField(default=timezone.now, verbose_name=_('date joined'))
    user_permissions = fields.ListField(
        fields.ReferenceField(auth.Permission),
        verbose_name=_('user permissions'),
        help_text=_('Permissions for the user.')
    )


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.username

    def __unicode__(self):
        return self.username

    def is_anonymous(self):
        return False

