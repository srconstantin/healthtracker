# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from tracker.models import Daily, Food, Activity, Medication, Supplement
from django.shortcuts import render_to_response
from django.http import Http404

def index(request):
    latest_days_list = Daily.objects.all().order_by('-date')[:10]
    return render_to_response('index.html', {'latest_days_list': latest_days_list})

def detail(request, day_id):
    try:
        d = Daily.objects.get(pk=day_id)
    except Daily.DoesNotExist:
        raise Http404
    return render_to_response('detail.html', {'daily': d}) 

def create(request, day_id):
    return HttpResponse("You just created Daily Log %s." % day_id)

def enter( request, day_id):
    return HttpResponse("You just entered an item in Daily Log %s." %day_id)

def results( request):
    return HttpResponse("These are your overall results.")


