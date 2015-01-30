from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):
  
 return render_to_response('home.html')
                             
                             

