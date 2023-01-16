from django.shortcuts import render

from voucher.models import Voucher


def generate(request):
    context = {}
    if request.GET:
        batch_nos = request.GET.get("batch_nos", "")
        batch_items = batch_nos.split(',')
        print(batch_items)

        context = {
            'vouchers': Voucher.objects.filter(is_enable=True, batch_no__in=batch_items)
        }

    return render(request, 'generate.html', context=context)
