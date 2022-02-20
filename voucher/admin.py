from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from voucher.models import Voucher
from voucher.resources import VoucherResource


class VoucherAdmin(ImportExportModelAdmin):
    list_display = ("datetime", "credits", "code", "price", "max",)
    resource_class = VoucherResource


admin.site.register(Voucher, VoucherAdmin)
