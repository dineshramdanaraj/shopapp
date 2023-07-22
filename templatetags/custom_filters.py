from django import template
from ..models import rating 
register = template.Library()

@register.filter
def get_item_rating(rate_item, item):
    try:
        return rate_item.get(item_to_rate=item)
    except rating.DoesNotExist:
        return None

@register.filter
def star_rating(value):
    try:
        value = int(value)
        full_stars = min(value, 5)
        empty_stars = 5 - full_stars
        return {'full_stars': full_stars, 'empty_stars': empty_stars}
    except ValueError:
        return None