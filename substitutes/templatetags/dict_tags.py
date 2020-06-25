from django import template

register = template.Library()


@register.filter
def get_item(dictionnary, key):

    return dictionnary.get(key)
