from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Merchant

@admin.register(Merchant)
class MerchantAdmin(ImportExportModelAdmin):
    pass
