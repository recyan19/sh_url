from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.conf import settings
from shortener.models import Url
from shortener.utils import get_short_code_for_url

from datetime import timedelta


def index(request):
    if request.method == "POST":
        url = request.POST.get('url', '')
        days = request.POST.get('days', '')

        try:
            days = int(days)
        except ValueError:
            days = 90

        url_id = get_short_code_for_url()
        if request.user.is_authenticated:
            url_object = Url.objects.create(url_id=url_id, url=url, days_to_expiry=days, created_by=request.user)
        else:
            url_object = Url.objects.create(url_id=url_id, url=url, days_to_expiry=days)
        expiry_date = url_object.date_created + timedelta(days=url_object.days_to_expiry)
        site_url = settings.SITE_URL

        return render(request, 'shortener/index.html', {'url_object': url_object, 'site_url': site_url, 'expiry_date': expiry_date})

    return render(request, 'shortener/index.html')


def get_original_url(request, url_id):
    url = get_object_or_404(Url, pk=url_id)

    if not url.check_expiry_date():
        return redirect(request.META['HTTP_REFERRER'])

    if any(url.url.strip().startswith(prt) for prt in ['https', 'http']):
        return HttpResponseRedirect(url.url.strip())
    else:
        if url.url.startswith('www.'):
            return HttpResponseRedirect('http://' + url.url.strip('www.'))
        return HttpResponseRedirect('http://' + url.url)


def user_urls_list(request):
    if request.user.is_authenticated:

        user_urls = Url.objects.filter(created_by=request.user)
        site_url = settings.SITE_URL

        return render(request, 'shortener/user_urls.html', {'user_urls': user_urls, 'site_url': site_url})

    return redirect('shortener:index')
