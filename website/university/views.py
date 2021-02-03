#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
#endregion

#region				   -----Type Hints-----
#endregion


#region				   -----Teacher views-----

def teacher_view(request, teacher_id):
    # TODO add database query for teacher
    teacher = None
    return render(request,'university/teacher.html',
                        context={'teacher':teacher})

#endregion


#region				   -----Faculty views-----

def faculty_view(request, faculty_id):
    # TODO add database query for faculty
    context = dict()
    faculty = None
    # context['faculty'] = faculty
    # if faculty.emblem:
    #     width, height = get_image_dimensions(instance.emblem.file)
    #     context['emblem_height'] = height
    #     context['emblem_width'] = width
    return render(request,'university/faculty.html',context=context)

#endregion