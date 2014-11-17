# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Url, MetaUrl

admin.site.register(Url)
admin.site.register(MetaUrl)
