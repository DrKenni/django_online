from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'

    return '/static/images/profile_nophoto.jpg'


@register.filter()
def limit_symbols(text):
    if text is None:
        return 'Без описания'
    elif len(text) > 50:
        return f'{text[:50]}...'
    else:
        return text
