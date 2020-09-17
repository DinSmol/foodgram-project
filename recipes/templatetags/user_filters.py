from django import template
# В template.Library зарегистрированы все теги и фильтры шаблонов
# добавляем к ним и наш фильтр
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
