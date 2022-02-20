from django import template

register = template.Library()


@register.filter
def zip_fill(data):
    return str(data).zfill(5)
