#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
from .services.service import StaffService
#endregion

#region				   -----Type Hints-----
#endregion

#region				   -----Teacher views-----

def teacher_view(request, teacher_id):
    # TODO add database query for teacher
    teacher = StaffService().get_staff(pk=teacher_id)
    return render(request,'university/teacher.html',
                        context={'teacher':teacher})

#endregion


#region				   -----Faculty views-----

def faculty_view(request, faculty_id):
    # TODO add database query for faculty
    context = dict()
    faculty = None
    teachers = None
    
    # if faculty.emblem:
    #     width, height = get_image_dimensions(instance.emblem.file)
    #     context['emblem_height'] = height
    #     context['emblem_width'] = width

    context['faculty'] = faculty
    context['teachers'] = teachers
    return render(request,'university/faculty.html',context=context)

#endregion