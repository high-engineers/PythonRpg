# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Race)
admin.site.register(Statistics)
admin.site.register(Condition)
admin.site.register(Skill)
admin.site.register(Entity)
admin.site.register(Npc)
admin.site.register(Character)
admin.site.register(User)
