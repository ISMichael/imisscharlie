from counter.models import Visit
from django.shortcuts import render_to_response
import datetime

def index(request):
	today = datetime.datetime.today()
	v = Visit.objects.get(id=1).visit_date
	delta = today-v
	days = delta.days
	return render_to_response('counter/index.html',{'days':days})

def charlieishere(request):
	v = Visit.objects.get(id=1)
	v.visit_date = datetime.datetime.today()
	v.save()
	return index(request)
