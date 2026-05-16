from django import template

register = template.Library()

@register.filter
def average(queryset, field_name):
    """
    Calculates the average of a field in a queryset.
    Usage: {{ recipe.ratings.all|average:"stars" }}
    """
    values = queryset.values_list(field_name, flat=True)
    if not values:
        return 0
    return round(sum(values) / len(values), 1)  # one decimal place