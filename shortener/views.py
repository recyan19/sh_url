from django.shortcuts import render
from django.shortcuts import render

from shortener.models import Url
from shortener.utils import get_short_code_for_url


def index(request):
    if request.method == "POST":
        url = request.POST.get('url', '')
        days = int(request.POST.get('days', ''))
        url_id = get_short_code_for_url()


        url_object = Url.objects.create(url_id=url_id, url=url, days_to_expiry=days)

        return render(request, 'shortener/index.html', {'url_object': url_object})

    return render(request, 'shortener/index.html')
