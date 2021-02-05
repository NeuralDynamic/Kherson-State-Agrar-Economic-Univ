#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
from .services.service import StaffService, FacultyService
#endregion

#region				   -----Type Hints-----
#endregion

#region				   -----Teacher views-----

def teacher_view(request, teacher_id):
    context = StaffService().get_staff(pk=teacher_id)
    return render(request,'university/teacher.html',
                        context=context)

#endregion


#region				   -----Faculty views-----

def faculty_view(request, faculty_id):
    # TODO add database query for faculty
    context = FacultyService().get_faculty(faculty_id)
    return render(request,'university/faculty.html',context=context)

#endregion


#region				   -----Faculty views-----

def cathedra_view(request, cathedra_id):
    # TODO add database query for cathedra
    context = dict()
    return render(request,'university/cathedra.html',context=context)

#endregion