from django.contrib import admin

# Register your models here.

from service.models import BTCUSD_info_model

admin.site.register(BTCUSD_info_model)