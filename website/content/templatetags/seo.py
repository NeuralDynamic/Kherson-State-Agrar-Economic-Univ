from content.seo import UniversitySite
from django.template import Library
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def seo_tags():
    try:
        site_seo = UniversitySite.objects.filter(primary=True).first()
    except UniversitySite.DoesNotExist:
        return ''
    if not site_seo:
        return ''
    return render_to_string('seo/seo_meta.html', {'seo':site_seo})
    