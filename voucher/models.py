from django.db import models


class Voucher(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    credits = models.TextField(max_length=80)
    code = models.TextField(max_length=80, primary_key=True)
    price = models.TextField(max_length=80)
    max = models.TextField(max_length=80)
