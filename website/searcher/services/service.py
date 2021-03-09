#region				-----External Imports-----
from django.db.models import Q
from django.utils.translation import get_language
from functools import reduce
from operator import or_
from typing import List
#endregion

#region				-----Internal Imports-----
from cms.models import Page, Title
from gallery.models import (Gallery, Image)
from library.models import Book
from news.models import (NewsFeed, Paper)
from university.models import (Cathedra,
Speciality, Faculty, Staff)
#endregion

class SearchService(object):
    models=[
            Gallery, 
            Image, 
            Book, 
            # NewsFeed, 
            Paper, 
            Cathedra, 
            # Faculty, don't have card for faculty
            Staff
            ]

    def search(self, phrase: str, language: str)->List[object]:
        """
        Searches phrase in all database\n
        :param phrase: phrase to search\n
        @return filled structure
        """
        words=phrase.split()
        result=type("", (), {})
        result.search_q=phrase
        result.search_result=False
        for model in self.models:
            #*Generates all necessary database queries
            query=Q()
            for word in words:
                for field in model().searching_fields():
                    query|=Q(**{f"{field}__icontains": word})

            #*Sets result of searching to structure
            search_result=(model.objects.filter(query).all())
            if search_result:
                result.search_result=True
                setattr(result, model.__name__.lower(),search_result)
        # search by cms pages
        cms_slugs=[]
        cms_pages = Page.objects.filter(publisher_is_draft=False).all()
        for cms_page in cms_pages:
            page_title_obj=Title.objects.filter(page_id=cms_page.pk, 
                                                language=language).first()
            if page_title_obj and phrase.lower() in page_title_obj.title.lower():
                print(phrase.lower(),page_title_obj.title.lower())
                cms_slugs.append(page_title_obj.slug)
                result.search_result=True
        result.pages_slugs=cms_slugs
        return result