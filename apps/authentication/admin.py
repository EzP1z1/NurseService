# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.users.models import CustomUser

from .models import Nurse


admin.site.register(CustomUser)
admin.site.register(Nurse)