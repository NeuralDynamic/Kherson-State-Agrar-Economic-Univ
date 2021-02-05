from django import template
from django.template.loader import get_template

from university.models import Faculty

register = template.Library()


def render_menu():
    faculties = Faculty.objects.prefetch_related('cathedras').all()
    return {'faculties':faculties}


t = get_template('menu.html')
register.inclusion_tag(t)(render_menu)