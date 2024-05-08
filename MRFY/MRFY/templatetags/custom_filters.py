from django import template

register = template.Library()

@register.filter
def split_string(value, delimiter):
    if not isinstance(value, str):
        return []
    return value.split(delimiter)

@register.filter
def custom_strip(value):
    if isinstance(value, str):
        return value.strip()
    return value
