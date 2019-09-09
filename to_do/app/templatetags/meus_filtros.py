from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, classValue):
    return value.as_widget(attrs={'class': classValue})