from django.shortcuts import render

from voucher.models import Voucher


def generate(request):
    context = {
        'vouchers': Voucher.objects.all()
    }
    return render(request, 'generate.html', context=context)
