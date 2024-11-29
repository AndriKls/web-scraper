from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .models import Link

def scrape_website(request):
    if request.method == 'POST':
        site = request.POST.get('site', '').strip()


        if not urlparse(site).scheme:
            site = 'http://' + site

        try:
            page = requests.get(site)
            soup = BeautifulSoup(page.text, 'html.parser')

            Link.objects.all().delete()

            for link in soup.find_all('a'):
                link_address = link.get('href')
                link_text = link.string
                if link_address:
                    Link.objects.create(address=link_address, name=link_text or "No Text")

            return HttpResponseRedirect('/')
        except requests.exceptions.RequestException as e:
            return render(request, 'myapp/error.html', {'error': str(e)})

    else:
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data': data})


def delete_urls(request):
    if request.method == 'POST':
        Link.objects.all().delete()
    return HttpResponseRedirect('/')