from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import urllib
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    file = settings.BUS_STATION_CSV
    with open(file, encoding='cp1251') as f:
        data = csv.DictReader(f)
        bus_stations_list = []
        for station in data:
            current_station = {'Name': station['Name'],
                               'Street': station['Street'],
                               'District': station['District']
                               }
            bus_stations_list.append(current_station)
    paginator = Paginator(bus_stations_list, 10)
    current_page = int(request.GET.get('page', 1))
    if current_page > paginator.num_pages:
        current_page = paginator.num_pages
    page = paginator.get_page(current_page)
    params = urllib.parse.urlencode({'page': current_page + 1})
    params_prev = urllib.parse.urlencode({'page': current_page + 1})
    next_page_url = reverse('bus_stations') + '?' + params
    prev_page_url = reverse('bus_stations') + '?' + params_prev

    return render(request, 'index.html', context={
        'bus_stations': page,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

