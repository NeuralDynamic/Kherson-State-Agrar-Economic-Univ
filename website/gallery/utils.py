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
    html="\n".join([f"""<img src='{image}' 
    style='display: inline-block; height: 70px; 
    width: 70px;'>""" for image in images])
    return format_html(html)

def reverse_related_url(model: str, id: int, 
title: str, app: str)->Html:
    """
    Displays link to the CRUD admin form\n
    :param title: title to show\n
    :param id: id of instance\n
    :param model: model name\n
    @return editing link
    """
    url=f"admin:{app}_{model}_change"
    link=reverse(viewname=url, args=[id])
    html=f"<a href='{link}'>{title}</a>"
    return format_html(html)