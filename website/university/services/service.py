from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

#region				-----External Imports-----
from library.models import Library, Book
from university.models import Staff
#endregion


class StaffService(object):
    def get_staff(self, pk: int)->object:
        try:
            context = dict()

            teacher = Staff.objects.select_related('links')\
                                    .select_related('library').get(pk=pk)
            context['teacher'] = teacher

            try:
                rewards = teacher.rewards.all()
                context['rewards'] = rewards
            except ObjectDoesNotExist:
                pass

            try:
                links = teacher.links.all()
                context['links'] = links
            except ObjectDoesNotExist:
                pass

            context['books'] = Book.objects.\
                    filter(library=teacher.library)
            

            return context
        except Staff.DoesNotExist:
            raise Http404