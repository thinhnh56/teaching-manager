# Create your views here.
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, Template
from apps.models import Subject, Lecturer, Scheduler, Scheduler_link, Program

def profile(request):
	if request.user.is_authenticated :
		return render_to_response("base.html")
	else:
		return HttpResponse("Failed")

def scheduler_link(request, schedule_name):
	schedule_list = Scheduler.objects.all()
	scheduler_link_list = Scheduler_link.objects.filter(scheduler__in = [Scheduler.objects.get(name = schedule_name),] )
	if request.POST:
		schedule_name = request.POST['schedule_name']
		scheduler_add(schedule_name)

	return render_to_response("schedule_list.html", 
								{'schedule_list':schedule_list, 'schedule_name':schedule_name, 'scheduler_link_list':scheduler_link_list},
								RequestContext(request))

def scheduler_add(name):
	new_scheduler = Scheduler()
	new_scheduler.name = name
	new_scheduler.save()

def scheduler(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	
	schedule_list = Scheduler.objects.all()

	if request.POST:
		schedule_name = request.POST['schedule_name']
		scheduler_add(schedule_name)

	return render_to_response("scheduler.html", {'schedule_list':schedule_list}, RequestContext(request))

#add new lecturer
def lecturer_add(name, falcuty, subjects_in_charge, subjects_can_teach, credits):
	new_lecturer = Lecturer()
	new_lecturer.name = name
	new_lecturer.falcuty = falcuty
	new_lecturer.credits = credits
	new_lecturer.save()
	
	for subject in subjects_in_charge:
		new_lecturer.subjects_in_charge.add(subject)

	for subject in subjects_can_teach:
		new_lecturer.subjects_can_teach.add(subject)


	new_lecturer.save()

def lecturer(request):

	if not request.user.is_authenticated:
		return HttpResponse('wrong')
	
	lecturer_list = Lecturer.objects.all()
	subjects_list =  Subject.objects.all()
	
	if request.POST:
		name = request.POST['lecturer_name']
		falcuty = request.POST['lecturer_falcuty']
		credit = request.POST['lecturer_credit']
		subjects_in_charge = request.POST.getlist('subjects_in_charge')
		subjects_can_teach = request.POST.getlist('subjects_can_teach')
		temp_list = []
		for subject in subjects_in_charge:
			temp_list.append(Subject.objects.get(name = subject))
		subjects_in_charge = []
		subjects_in_charge = temp_list
		temp_list = []
		for subject in subjects_can_teach:
			temp_list.append(Subject.objects.get(name = subject))
		subjects_can_teach = []
		subjects_can_teach = temp_list
		lecturer_add(name, falcuty, subjects_in_charge, subjects_can_teach, credit)

	return render_to_response("lecturer.html", {"lecturer_list" : lecturer_list, "subjects_list" : subjects_list}, RequestContext(request))
	
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