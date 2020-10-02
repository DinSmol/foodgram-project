from django import template


register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def addrows(field, css):
    return field(attrs={"rows": css})


@register.filter(name='get_filter_values')
def get_filter_values(value):
    return value.getlist('filters')

	
@register.filter(name='is_favorite')
def get_filter_values(value):
    return value.getlist('filters')

    user = request.user
    if user.is_authenticated:
        favourite_ids = [item.id for item in user.user_favourites.all()]
        return favourite_ids
    return None