# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Beach


def index(request):
    return HttpResponse('Placeholder home page') 
    

def get_report(request, beach_id):
    try:
        beach = Beach.objects.get(id = beach_id)
        return render(request, 'report/report.html', {'beach': beach})

    except Beach.DoesNotExist:
        raise Htpp404("404")
