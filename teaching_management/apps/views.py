# Create your views here.
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render_to_response

def profile(request):
	if request.user.is_authenticated :
		return render_to_response("base.html")
	else:
		return HttpResponse("Failed")
		
def scheduler(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
		
	return render_to_response("scheduler.html" )
	
def lecturer(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	return render_to_response("lecturer.html")
	
	
def subject(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	return render_to_response("subject.html")
	
def program(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	return render_to_response("program.html")
	
def statistic(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	return render_to_response("statistic.html")