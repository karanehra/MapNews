from django.http import HttpResponse
import datetime 
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from functions import *

@csrf_exempt
def getnews(request):
	if request.method == "POST":
		address = request.body
		address = address.split(".")  
		address.pop()
		address_dupl = address
		for item in address:
			if item.isdigit():
				address_dupl.remove(item)
		address = address_dupl
		return HttpResponse(address)	
	return HttpResponse("<html><body>hello</body></html>")

def index(request):
	t = get_template('map.html')
	return HttpResponse(t.render())

def signup_screen(request):
	if request.method == "GET":
		t= get_template('signup.html')
		return HttpResponse(t.render())
