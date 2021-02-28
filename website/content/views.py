from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils.translation import ugettext_lazy as _

from .forms import ContactRequestForm
from .service.manifest import generate_manifest


def manifest_view(request):
    manifest_json = generate_manifest()
    return JsonResponse(manifest_json)


def contact_form_request(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    form = ContactRequestForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({'status':'OK','message':_('Спасибо, мы ответим как только сможем!')})
    else:
        return JsonResponse({'status':'BAD','message':'Form is not valid'})


def custom_template_handler404(request, exception):
    return render(request, 'errors/404.html')

def custom_template_handler500(request):
    return render(request, 'errors/500.html')