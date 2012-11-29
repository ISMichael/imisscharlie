from counter.models import Visit
from django.shortcuts import render_to_response

def index(request):
	v = Visit.objects.get(id=1).visit_date
	return render_to_response('counter/index.html',{'days':v})


