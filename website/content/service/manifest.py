from content.seo import UniversitySite
from django.conf import settings
import json


def generate_manifest():
    template_path = f'{settings.STATIC_ROOT}/manifest.json'

    with open(template_path) as fin:
        json_data = json.load(fin)
        json_data['short_name'] = "KSAEU"
        json_data['name'] = "Kherson State Agrarian and Economic University"

        univesity_seo = UniversitySite.objects.filter(primary=True).first()
        if univesity_seo:
            univesity_seo.set_current_language('en')
            json_data['description'] = univesity_seo.description

        fin.close()

        return json_data

