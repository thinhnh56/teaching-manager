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

#add scheduler_link function
def add_scheduler_link(scheduler, subject, lecturer_list):
	new_scheduler_link = Scheduler_link()
	new_scheduler_link.scheduler = scheduler
	new_scheduler_link.subject = subject
	new_scheduler_link.save()					#add contents of schuedule link
	for lecturer in lecturer_list:
		new_scheduler_link.lecturer.add(lecturer)
	new_scheduler_link.save()

#link scheduler info to database and vice versa
def scheduler_link(request, schedule_name):
	schedule_list = Scheduler.objects.all()
	scheduler_link_list = Scheduler_link.objects.filter(scheduler__in = [Scheduler.objects.get(name = schedule_name),] )
	lecturer_list = Lecturer.objects.all()
	subject_list = Subject.objects.all()
	if request.POST:
		if request.POST['form_type'] == 'new_schedule' :
			schedule_name = request.POST['schedule_name']
			scheduler_add(schedule_name)							
		elif request.POST['form_type'] == 'add_link':
			scheduler = Scheduler.objects.get(name = schedule_name)			
			subject_ID = request.POST['subject_ID']						
			subject = Subject.objects.get(ID = subject_ID)
			lecturers = request.POST.getlist('lecturers')
			temp_list = []
			for lec in lecturers :
				temp_list.append(Lecturer.objects.get(name = lec))
			lecturers = temp_list
			add_scheduler_link(scheduler, subject, lecturers)

	return render_to_response("schedule_list.html", 
								{'lecturer_list':lecturer_list, 'subject_list':subject_list, 
								'schedule_list':schedule_list, 'schedule_name':schedule_name, 'scheduler_link_list':scheduler_link_list},
								RequestContext(request))

#add schedule function
def scheduler_add(name):
	new_scheduler = Scheduler()
	new_scheduler.name = name
	new_scheduler.save()

#scheduler page
def scheduler(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')			#if wrong url
	
	schedule_list = Scheduler.objects.all()

	if request.POST:
		schedule_name = request.POST['schedule_name']
		scheduler_add(schedule_name)

	return render_to_response("scheduler.html", {'schedule_list':schedule_list}, RequestContext(request))

#add new lecturer function
def lecturer_add(name, falcuty, subjects_in_charge, subjects_can_teach, credits):
	new_lecturer = Lecturer()
	new_lecturer.name = name
	new_lecturer.falcuty = falcuty					#add contents of lecturer
	new_lecturer.credits = credits
	new_lecturer.save()
	
	for subject in subjects_in_charge:
		new_lecturer.subjects_in_charge.add(subject)		#add some subjects a lecturer is teaching

	for subject in subjects_can_teach:
		new_lecturer.subjects_can_teach.add(subject)		#add some subjects a lecturer can teach


	new_lecturer.save()

#lecturer page
def lecturer(request):

	if not request.user.is_authenticated:		#if wrong url
		return HttpResponse('wrong')
	
	lecturer_list = Lecturer.objects.all()
	subjects_list =  Subject.objects.all()
	
	if request.POST:
		name = request.POST['lecturer_name']
		falcuty = request.POST['lecturer_falcuty']						#all contents of lecturer
		credit = request.POST['lecturer_credit']
		subjects_in_charge = request.POST.getlist('subjects_in_charge')
		subjects_can_teach = request.POST.getlist('subjects_can_teach')
		temp_list = []
		for subject in subjects_in_charge:
			temp_list.append(Subject.objects.get(name = subject))
		subjects_in_charge = []
		subjects_in_charge = temp_list								#display subject a lecturer is teaching
		temp_list = []
		for subject in subjects_can_teach:
			temp_list.append(Subject.objects.get(name = subject))		#display subject a lecturer can teach
		subjects_can_teach = []
		subjects_can_teach = temp_list
		lecturer_add(name, falcuty, subjects_in_charge, subjects_can_teach, credit)

	return render_to_response("lecturer.html", {"lecturer_list" : lecturer_list, "subjects_list" : subjects_list}, RequestContext(request))
	
#add new subject function
def subject_add(name, ID, program, credit):
	new_subject = Subject()
	new_subject.name = name					#add contents of subject
	new_subject.ID = ID
	new_subject.program = program
	new_subject.credits = credit
	new_subject.save()

#subject page
def subject(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')			#if wrong url
	subject_list = Subject.objects.all()
	program_list = Program.objects.all()	
	if request.POST:							#if true url
		name = request.POST['subject_name']
		ID = request.POST['subject_ID']
		credit = request.POST['subject_credit']			#display contents of subject
		program = request.POST['subject_program']
		program = Program.objects.get(name = program)
		subject_add(name, ID, program, credit)
	return render_to_response("subject.html", {"subject_list" : subject_list, 'program_list':program_list}, RequestContext(request))

#Program page
def program(request):
	if not request.user.is_authenticated:
		return HttpResponse('wrong')				#if wrong url
	return render_to_response("program.html")

#Statistic page	
def statistic(request):
	if not request.user.is_authenticated:			#if wrong url
		return HttpResponse('wrong')
	return render_to_response("statistic.html")