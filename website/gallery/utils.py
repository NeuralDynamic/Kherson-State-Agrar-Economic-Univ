#region             -----External Imports-----
from django.utils.html import format_html
from typing import TypeVar, List
from django.urls import reverse
#endregion

#region                -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

#region             -----Render Functions-----
def render_related_images(images: List[str])->Html:
    """
    Generates and beautifies HTML code
    for displaying related images\n
    :param images: list of images\n
    @return rendered HTML page
    """
    html=[f"""<img src='{image}' style='
    height: 70px; width: 70px'; 
    display: inline-block;">"""
    for image in images]
    return format_html("\n".join(html))

def reverse_related_url(model: str, id: int, 
title: str)->Html:
    """
    Displays the title of model and
    link to the CRUD admin form\n
    :param title: title to show\n
    :param id: id of instance\n
    :param model: model name\n
    @return editing link
    """
    url=f"admin:gallery_{model}_change"
    link=reverse(viewname=url, args=[id])
    html=f"<a href='{link}'>{title}</a>"
    return format_html(html)
#endregion