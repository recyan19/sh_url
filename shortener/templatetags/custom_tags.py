from datetime import timedelta

from django import template

register = template.Library()


@register.filter
def plus_days(value, days):
    return value + timedelta(days=days)
