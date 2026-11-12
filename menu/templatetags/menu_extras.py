from django import template

register = template.Library()


@register.filter
def currency(value):
    """Turn a number into money text. Example: 5.5 -> "$5.50"."""
    return f"${value:,.2f}"
