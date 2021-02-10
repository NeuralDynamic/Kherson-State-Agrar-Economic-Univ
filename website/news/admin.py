#region				-----External Imports-----
from django.contrib.admin import register
from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.shortcuts import redirect
from django.utils.html import format_html
#endregion

#region				-----Internal Imports-----
from .models import NewsFeed, Paper
#endregion

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
    "news_feed", "gallery"]
    list_display=["__str__", "_news_feed", 
    "_gallery", "preview"]
    list_filter=["news_feed__translations__title",
    "gallery__translations__title"]
    #endregion

    #region         -----Internal Methods-----
    def response_change(self, request, obj):
        if "_preview" in request.POST:
            return redirect(obj.get_absolute_url())
        return super().response_change(request, obj)
    def preview(self, obj)->str:
        return format_html(
            f"""<a class="button" target=_blank
            href={obj.get_absolute_url()}>Preview</a>"""
        )
    #endregion