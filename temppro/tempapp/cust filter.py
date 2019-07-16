from django import template
register=template.libary()

def first_eight_upper(value):
    result=value[:8].upper()
    return result
register.filter('f8upper',first_eight_upper)
