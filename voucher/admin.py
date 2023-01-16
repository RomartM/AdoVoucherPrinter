from django import forms
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.forms import ImportForm

from voucher.models import Voucher
from voucher.resources import VoucherResource


@admin.action(description='Mark selected schedules as enabled')
def make_enable(modeladmin, request, queryset):
    queryset.update(is_enable=True)


@admin.action(description='Mark selected schedules as disabled')
def make_disable(modeladmin, request, queryset):
    queryset.update(is_enable=False)


class VoucherImportForm(ImportForm):
    batch_no = forms.CharField(max_length=30)


class VoucherAdmin(ImportExportModelAdmin):
    list_display = ("datetime", "credits", "code", "price", "max", "batch_no", "is_enable")
    list_filter = ("batch_no",)
    actions = [make_enable, make_disable]
    resource_class = VoucherResource

    def get_import_form(self):
        return VoucherImportForm

    # Send the extra value to the resource constructor using kwargs.
    # This overrides an existing hook method in `ImportMixin`.
    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        # This method may be called by the initial form GET request, before
        # the batch_no is chosen. So we default to None.
        rk['batch_no'] = None
        if request.POST:  # *Now* we should have a non-null value
            # In the dry-run import, the batch_no is included as a form field.
            batch_no = request.POST.get('batch_no', None)
            if batch_no:
                # If we have it, save it in the session so we have it for the confirmed import.
                request.session['batch_no'] = batch_no
            else:
                try:
                    # If we don't have it from a form field, we should find it in the session.
                    batch_no = request.session['batch_no']
                except KeyError as e:
                    raise Exception("Context failure on row import, " +
                                    f"check admin.py for more info: {e}")
            rk['batch_no'] = batch_no
        return rk


admin.site.register(Voucher, VoucherAdmin)
