from django.db import models


class Voucher(models.Model):
    is_enable = models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now=True)
    batch_no = models.CharField(max_length=30, default="")
    credits = models.TextField(max_length=80)
    code = models.TextField(max_length=80, primary_key=True)
    price = models.TextField(max_length=80)
    max = models.TextField(max_length=80)
