#region				-----External Imports-----
from django.shortcuts import render
from typing import (Dict, TypeVar)
#endregion

#region				-----Internal Imports-----
from .services.service import (StaffService, 
FacultyService, CathedarService)
#endregion

#region				   -----Type Hints-----
Html=TypeVar("Html", str, bytes)
#endregion

#region				 -----Cathedra views-----
def cathedra_view(request: Dict, cathedra_id: int)->Html:
    """
    Renders cathedra template page using cathedra id\n
    :param cathedra_id: id of cathedra\n
    :param request: Http request\n
    @return built template
    """
    context=CathedarService().get_cathedra(pk=cathedra_id)
    return render(request=request, context=context,
    template_name='university/cathedra.html')
#endregion

#region				 -----Teacher views-----
def teacher_view(request: Dict, teacher_id: int)->Html:
    """
    Renders teacher template page using teacher id\n
    :param teacher_id: id of teacher\n
    :param request: Http request\n
    @return built template
    """
    context = StaffService().get_staff(pk=teacher_id)
    return render(request=request, context=context,
    template_name='university/teacher.html')
#endregion

#region				 -----Faculty views-----
def faculty_view(request: Dict, faculty_id: int)->Html:
    """
    Renders faculty template page using faculty id\n
    :param faculty_id: id of faculty\n
    :param request: Http request\n
    @return built template
    """
    context=FacultyService().get_faculty(faculty_id)
    return render(request=request, context=context,
    template_name='university/faculty.html')
#endregion