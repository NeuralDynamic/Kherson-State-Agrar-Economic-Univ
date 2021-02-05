#region				-----External Imports-----
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from library.models import Library, Book
from university.models import Staff, Faculty
#endregion

class FacultyService(object):
    def  get_faculty(self, pk: int)->object:
        try:
            context = dict()

            faculty = (Faculty.objects
            .prefetch_related('scientific_society')
            .prefetch_related('cathedras')
            .prefetch_related('gallery')
            .get(pk=pk))

            context['faculty'] = faculty

            try:
                teachers = faculty.staff.all()
                print(teachers)
                context['teachers'] = teachers
            except ObjectDoesNotExist:
                pass

            try:
                scientific_society = faculty.scientific_society.staff.all()
                print(scientific_society)
                context['scientific_society'] = scientific_society
            except ObjectDoesNotExist:
                pass

            try:
                cathedras = faculty.cathedras.all()
                print(cathedras)
                context['cathedras'] = cathedras
            except ObjectDoesNotExist:
                pass

            try:
                gallery = faculty.gallery.images.all()
                print(gallery)
                context['gallery'] = gallery
            except ObjectDoesNotExist:
                pass
            
            return context
        except Faculty.DoesNotExist:
            raise Http404

class StaffService(object):
    def get_staff(self, pk: int)->object:
        try:
            context = dict()

            teacher = Staff.objects.select_related('links')\
                                    .select_related('library').get(pk=pk)
            context['teacher'] = teacher

            try:
                rewards = teacher.rewards.all()
                print(rewards)
                context['rewards'] = rewards
            except ObjectDoesNotExist:
                pass

            try:
                links = teacher.links
                context['links'] = links
            except ObjectDoesNotExist:
                pass

            try:
                disciplines = teacher.disciplines.all()
                context['disciplines'] = disciplines
            except ObjectDoesNotExist:
                pass

            context['books'] = Book.objects.\
                    filter(library=teacher.library)
            

            return context
        except Staff.DoesNotExist:
            raise Http404