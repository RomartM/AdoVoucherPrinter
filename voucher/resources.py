from import_export import resources, fields
from import_export.widgets import CharWidget

from voucher.models import Voucher


class VoucherResource(resources.ModelResource):
    credits = fields.Field(attribute='credits', column_name='﻿Time/Data/Credits', widget=CharWidget())
    code = fields.Field(attribute='code', column_name='Voucher Code', widget=CharWidget())
    price = fields.Field(attribute='price', column_name='Price', widget=CharWidget())
    max = fields.Field(attribute='max', column_name=' Max. Users', widget=CharWidget())

    class Meta:
        model = Voucher
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('code',)
        exclude = ('id', 'datetime',)
        fields = (
            'credits',
            'code',
            'price',
            'max',
        )
