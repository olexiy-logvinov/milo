from django import template
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag
def allowed(profile):
    if profile.allowed():
        return mark_safe('<span class="label label-success">allowed</span>')
    return mark_safe('<span class="label label-danger">blocked</span>')


@register.simple_tag
def bizzfuzz(profile):
    bf_map = {
        'Bizz': '<span class="label label-info">Bizz</span>',
        'Fuzz': '<span class="label label-warning">Fuzz</span>',
        'BizzFuzz': '<span class="label label-success">BizzFuzz</span>',
        '': ''
    }
    return mark_safe(bf_map[profile.bizz_fuzz()])
