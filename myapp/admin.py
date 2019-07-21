# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#
#
from django.contrib import admin
from . models import *


admin.site.register(contact)
admin.site.register(package)


admin.site.register(webpage)

