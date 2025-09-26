import locale

from django import template


register = template.Library()


@register.filter
def money_format(value):
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(value, grouping=True, symbol=False)
    except:
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
