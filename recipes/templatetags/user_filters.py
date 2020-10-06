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
def is_favorite(value, user):
    if user.is_anonymous: return False
    return user.user_favourites.filter(id=value).exists()


@register.filter(name='is_follow')
def is_follow(author, user):
    if user.is_anonymous: return False
    return user.user_followers.filter(author=author).exists()
