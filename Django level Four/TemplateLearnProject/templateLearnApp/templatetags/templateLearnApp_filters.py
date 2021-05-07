from django import template

register = template.Library()


@register.filter(name='con')
def con(value, arg):
    """
    This concates the "args" 3 times
    """
    arg = ' '+arg
    return value + arg*3


#register.filter('conX3', concateX3)
