from django.shortcuts import render
from django.http import JsonResponse
from .service.manifest import generate_manifest


def manifest_view(request):
    manifest_json = generate_manifest()
    return JsonResponse(manifest_json)
