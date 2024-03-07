from django import template


register = template.library


@register.filter()
def media_filter(data):
    if data:
        return f'/media/{data}'
    return '#'
