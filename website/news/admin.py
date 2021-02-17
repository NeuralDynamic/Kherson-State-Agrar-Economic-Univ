#region				-----External Imports-----
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.shortcuts import redirect
from django.utils.html import format_html
from typing import (Dict, TypeVar)
#endregion

#region				-----Internal Imports-----
from .models import NewsFeed, Paper, Categories
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

@register(Categories)
class CategoriesAdmin(TranslatableAdmin): pass

@register(NewsFeed)
class NewsFeedAdmin(TranslatableAdmin):
    #region           ----Configuration-----
    fields=["title", "description", "_papers"]
    readonly_fields=["_papers"]
    list_display=["__str__"]
    #endregion

@register(Paper)
class PaperAdmin(TranslatableAdmin):
    change_form_template="admin/news/change_form.html"

    #region           ----Configuration-----
    ordering = ['created_at']
    fields=["header", "title", "story", 
    "news_feed", "gallery", "category"]
    list_display=["__str__", "_news_feed", 
    "_gallery", "preview", "category"]
    list_filter=["news_feed__translations__title",
    "gallery__translations__title", "category"]
    #endregion

    #region         -----Internal Methods-----
    def response_change(self, request: Dict, 
    obj: object)->Html:
        """
        Creates preview button in CRUD admin form\n
        :param request: Http request\n
        @return generated button
        """
        if "_preview" in request.POST:
            return redirect(obj.get_absolute_url())
        return super().response_change(
        request=request, obj=obj)

    def preview(self, obj: object)->Html:
        """
        Creates preview button on list page\n
        :param obj: model instance\n
        @return generated button
        """
        return format_html(f"""<a class="button"
        href={obj.get_absolute_url()}
        target=_blank>Preview</a>""")
    #endregion