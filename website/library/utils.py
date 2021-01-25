#region             -----External Imports-----
from django.utils.html import format_html
from typing import TypeVar, List
from django.urls import reverse
#endregion

#region                -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

#region             -----Render Functions-----
def render_related_books(books: List[str])->Html:
    """
    Generates and beautifies HTML code
    for displaying related books\n
    :param books: list of books\n
    @return rendered HTML page
    """
    html="<ul>"+"\n".join([f"<li>{book}</li>"
    for book in books])+"</ul>"
    return format_html(html)
#endregion