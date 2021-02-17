#region				-----External Imports-----
from django.db.models import Q
from functools import reduce
from operator import or_
from typing import List
#endregion

#region				-----Internal Imports-----
from gallery.models import (Gallery, Image)
from library.models import Book
from news.models import (NewsFeed, Paper)
from university.models import (Cathedra,
Speciality, Faculty, Staff)
#endregion

class SearchService(object):
    models=[Gallery, Image, Book, NewsFeed,
    Paper, Cathedra, Speciality, Faculty, Staff]

    def search(self, phrase: str)->List[object]:
        """
        Searches phrase in all database\n
        :param phrase: phrase to search\n
        @return filled structure
        """
        words=phrase.split()
        result=type("", (), {})
        for model in self.models:
            #*Generates all necessary database queries
            query=Q()
            for word in words:
                for field in model().searching_fields():
                    query|=Q(**{f"{field}__icontains": word})

            #*Sets result of searching to structure
            setattr(result, model.__name__.lower(),
            (model.objects.filter(query)))
        print(result.staff)
        return result.staff