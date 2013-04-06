# Create your views here.
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from apps.models import Subject, Lecturer, Scheduler, Program

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
	lecturer_list = Lecturer.objects.all()
	return render_to_response("lecturer.html", {"lecturer_list" : lecturer_list})
	
#add new subject
def subject_add(name, ID, program, credit):
	new_subject = Subject()
	new_subject.name = name
	new_subject.ID = ID
	new_subject.program = program
	new_subject.credits = credit
	new_subject.save()

def subject(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	subject_list = Subject.objects.all()
	program_list = Program.objects.all()	
	if request.POST:
		name = request.POST['subject_name']
		ID = request.POST['subject_ID']
		credit = request.POST['subject_credit']
		program = request.POST['subject_program']
		program = Program.objects.get(name = program)
		subject_add(name, ID, program, credit)
	return render_to_response("subject.html", {"subject_list" : subject_list, 'program_list':program_list}, RequestContext(request))
	
def program(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	return render_to_response("program.html")
	
def statistic(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	return render_to_response("statistic.html")