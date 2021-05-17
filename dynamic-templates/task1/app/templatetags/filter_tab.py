from django import template
import csv

register = template.Library()


@register.filter()
def color(item, last_item=''):
    if last_item == 'Last':
        try:
            item_1 = float(item)
            return 'Gray'
        except Exception:
            return ''
    if item == '':
        return ''
    try:
        item_1 = float(item)
        if item_1 < 0:
            return 'green'
        elif 1 <= item_1 < 2:
            return '#F08080'
        elif 2 <= item_1 < 5:
            return '#DC143C'
        elif item_1 >= 5:
            return '#8B0000'
        elif item_1 >= 1500:
            return ''
        else:
            return ''
    except Exception:
        return ''


@register.filter()
def is_empty(item):
    if item == '':
        return '-'
    else:
        return item


@register.filter()
def last(row):
    return row[-1]
