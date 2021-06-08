#region				-----External Imports-----
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from library.models import Book
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

            context['cathedra']=cathedra

            try:
                teachers = StaffCathedra.objects.select_related("staff")\
                    .filter(cathedras=cathedra.pk).all()
                context['teachers'] = teachers
            except Exception:
                pass

            try:
                gallery = cathedra.gallery.images.all()
                context['gallery'] = gallery
            except Exception:
                pass

            try:
                matherial_base = cathedra.material_technical_base.all()
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

            context['faculty'] = faculty

            try:
                teachers = StaffFaculty.objects.select_related("staff")\
                    .filter(faculties=faculty.pk).all()
                context['teachers'] = teachers
            except Exception:
                pass

            try:
                scientific_society = faculty.scientific_society.staff.all()
                context['scientific_society'] = scientific_society
            except Exception:
                pass

            try:
                cathedras = faculty.cathedras.all()
                context['cathedras'] = cathedras
            except Exception:
                pass

            try:
                gallery = faculty.gallery.images.all()
                context['gallery'] = gallery
            except Exception:
                pass

            specialities = Speciality.objects.order_by('educational_level').\
                filter(cathedra__faculty__pk=faculty.pk).all()
            specialities_list = list()
            specialities_dict = dict()
            current = None

            for speciality in specialities:
                if not current:
                    current = speciality.get_educational_level_display()

                if current == speciality.get_educational_level_display():
                    specialities_list.append(speciality)
                else:
                    specialities_dict[current] = specialities_list
                    current = speciality.get_educational_level_display()
                    specialities_list = []
                    specialities_list.append(speciality)

            specialities_dict[current] = specialities_list
            del current
            context['specialities_dict'] = specialities_dict
            
            return context
        except Faculty.DoesNotExist:
            raise Http404

class StaffService(object):
    def get_staff(self, pk: int)->object:
        try:
            context = dict()

            teacher = Staff.objects.get(pk=pk)
            context['teacher'] = teacher

            try:
                rewards = teacher.rewards.all()
                context['rewards'] = rewards
            except ObjectDoesNotExist:
                pass

            try:
                disciplines = teacher.disciplines.all()
                context['disciplines'] = disciplines
            except ObjectDoesNotExist:
                pass

            context['books'] = teacher.books.all()
            
            return context
        except Staff.DoesNotExist:
            raise Http404