#region				-----External Imports-----
from django.shortcuts import render
#endregion

#region				-----Internal Imports-----
#endregion

#region				   -----Type Hints-----
#endregion


#region				   -----Teacher views-----

def teacher_view(request, teacher_id):
    return render(request,'university/teacher.html')

#endregion