#region				-----External Imports-----
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from library.models import Library, Book
from university.models import (Staff, Faculty, StaffFaculty, 
Speciality, Cathedra, StaffCathedra)
#endregion

class CathedarService(object):
    def get_cathedra(self, pk: int)->object:
        try:
            context = dict()

            cathedra = (Cathedra.objects
            .prefetch_related('gallery')
            .get(pk=pk))

            print(cathedra)
            context['cathedra']=cathedra

            try:
                teachers = StaffCathedra.objects.select_related("staff")\
                    .filter(cathedras=cathedra.pk).all()
                print(teachers)
                context['teachers'] = teachers
            except Exception:
                pass

            try:
                gallery = cathedra.gallery.images.all()
                print(gallery)
                context['gallery'] = gallery
            except Exception:
                pass

            try:
                matherial_base = cathedra.material_technical_base.all()
                print(matherial_base)
                context['matherial_base'] = matherial_base
            except Exception:
                pass

            return context
        except Cathedra.DoesNotExist:
            raise Http404

class FacultyService(object):
    def get_faculty(self, pk: int)->object:
        try:
            context = dict()

            faculty = (Faculty.objects
            .prefetch_related('scientific_society')
            .prefetch_related('cathedras')
            .prefetch_related('gallery')
            .get(pk=pk))

            print(faculty)
            context['faculty'] = faculty

            try:
                teachers = StaffFaculty.objects.select_related("staff")\
                    .filter(faculties=faculty.pk).all()
                print(teachers)
                context['teachers'] = teachers
            except Exception:
                pass

            try:
                scientific_society = faculty.scientific_society.staff.all()
                print(scientific_society)
                context['scientific_society'] = scientific_society
            except Exception:
                pass

            try:
                cathedras = faculty.cathedras.all()
                print(cathedras)
                context['cathedras'] = cathedras
            except Exception:
                pass

            try:
                gallery = faculty.gallery.images.all()
                print(gallery)
                context['gallery'] = gallery
            except Exception:
                pass

            try:
                specialities = Speciality.objects.filter(cathedra__faculty__pk=faculty.pk)
                print(specialities)
                context['specialities'] = specialities
            except Exception:
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