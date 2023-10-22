from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Country

# Create your views here.


def countries(request):
    countries= Country.objects.all().values()
    template = loader.get_template('countries-list.html')
    context={
        'countries':countries
    }
    
    return HttpResponse(template.render(context, request))

def detail(request, id):
    country= Country.objects.get(id=id)
    template = loader.get_template('country-details.html')
    context={
        'country':country
    }
    
    return HttpResponse(template.render(context, request))