""""
View handle request from user
and display response
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.models import Subject, Lecturer, Scheduler, Scheduler_link, Program, Lecturer_teaching_info

def profile(request):
    if request.user.is_authenticated :
        return render_to_response("base.html")
    else:
        return HttpResponse("Failed")
    
def update_lecturer_teaching_info(lecturer, subject):
    """
    add lecturer_teaching_info to database:
    lecturer: a lecturer object
    subject: a subject object
    """
    try :
        currentLecturer = Lecturer_teaching_info.objects.get(lecturer__in = [lecturer,])
        currentLecturer.update(subject)
    except Lecturer_teaching_info.DoesNotExist :
        currentLecturer = Lecturer_teaching_info()
        currentLecturer.credit = 0
        currentLecturer.lecturer = lecturer
        currentLecturer.save()
        currentLecturer.update(subject)
        currentLecturer.save()
        
        
#add scheduler_link function
def add_scheduler_link(scheduler, subject, lecturer_list):
    """
    add a scheduler_link to database
    (link scheduler, subject and lecturer_list)
    scheduler : a scheduler object
    subject : a subject object
    lecturer_list: a list of lecturer object
    """
    new_scheduler_link = Scheduler_link()
    new_scheduler_link.scheduler = scheduler
    new_scheduler_link.subject = subject
    new_scheduler_link.save()                    #add contents of schuedule link
    for lecturer in lecturer_list:
        new_scheduler_link.lecturer.add(lecturer)
        #every time assign subject to a lecturer we wil update lecturer's teaching infomation
        update_lecturer_teaching_info(lecturer, subject)
    new_scheduler_link.save()

#link scheduler info to database and vice versa
def scheduler_link(request, schedule_name):
    """"
    link three element
    link subject with lecturers and scheduler
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')                #if wrong user
    schedule_list = Scheduler.objects.all()
    scheduler_link_list = Scheduler_link.objects.filter(
                                scheduler__in = 
                                    [Scheduler.objects.get(name = schedule_name),] )
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
                                {'lecturer_list':lecturer_list, 
                                'subject_list':subject_list, 
                                'schedule_list':schedule_list, 
                                'schedule_name':schedule_name, 
                                'scheduler_link_list':scheduler_link_list},
                                RequestContext(request))

#add schedule function
def scheduler_add(name):
    """
    add new scheduler
    name : name of a scheduler (string)
    """
    new_scheduler = Scheduler()
    new_scheduler.name = name
    new_scheduler.save()

#scheduler page
def scheduler(request):
    """
    scheduler view for scheduler page
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')            #if wrong url
    
    schedule_list = Scheduler.objects.all()
    
    if request.POST:
        schedule_name = request.POST['schedule_name']
        scheduler_add(schedule_name)
    
    return render_to_response("scheduler.html", 
                                {'schedule_list':schedule_list}, 
                                RequestContext(request))

#add new lecturer function
def lecturer_add(name, faculty, subjects_in_charge, subjects_can_teach, credit):
    """
    add a new lecturer to database:
    name : name of a lecturer (string)
    faculty : name of lecturer's faculty
    subjects_in_charge : a list of subject object
    subjects_can_teach : a list of subject object
    credit: amount of credits assigned to lecturer (number)
    """
    new_lecturer = Lecturer()
    new_lecturer.name = name
    #add contents of lecturer
    new_lecturer.faculty = faculty                    
    new_lecturer.credits = credit
    new_lecturer.save()
    
    for subject in subjects_in_charge:
        #add some subjects a lecturer is teaching
        new_lecturer.subjects_in_charge.add(subject)        
    
    for subject in subjects_can_teach:
        #add some subjects a lecturer can teach
        new_lecturer.subjects_can_teach.add(subject)        
    
    
    new_lecturer.save()


def lecturer(request):
    """
    lecturer view for lecturer page
    receive request from user 
    if request has POST then handle form
    """
    #if wrong user
    if not request.user.is_authenticated:        
        return HttpResponse('wrong')
    
    lecturer_list = Lecturer.objects.all()
    subjects_list =  Subject.objects.all()
    
    if request.POST:
        name = request.POST['lecturer_name']
        #all contents of lecturer
        faculty = request.POST['lecturer_faculty']                        
        credit = request.POST['lecturer_credit']
        subjects_in_charge = request.POST.getlist('subjects_in_charge')
        subjects_can_teach = request.POST.getlist('subjects_can_teach')
        temp_list = []
        for subject in subjects_in_charge:
            temp_list.append(Subject.objects.get(name = subject))
        subjects_in_charge = []
        #display subject a lecturer is teaching
        subjects_in_charge = temp_list                                
        temp_list = []
        for subject in subjects_can_teach:
            #display subject a lecturer can teach
            temp_list.append(Subject.objects.get(name = subject))        
        subjects_can_teach = []
        subjects_can_teach = temp_list
        lecturer_add(name, faculty, subjects_in_charge, 
                                    subjects_can_teach, credit)
    
    return render_to_response("lecturer.html", 
                                {"lecturer_list" : lecturer_list, 
                                "subjects_list" : subjects_list},
                                     RequestContext(request))
    
#add new subject function
def subject_add(name, ID, program, credit):
    """
    add new subject to database with:
    name : name of a subject ( string )
    ID : identifier of a subject (string)
    program : exist program object in databse (Program object)
    creidt : credit of a subject  (number)
    """
    new_subject = Subject()
    new_subject.name = name                    #add contents of subject
    new_subject.ID = ID
    new_subject.program = program
    new_subject.credits = credit
    new_subject.save()

#subject pageh
def subject(request):
    """
    function display for subject page
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')            #if wrong url
    subject_list = Subject.objects.all()
    program_list = Program.objects.all()    
    if request.POST:                            #if true url
        name = request.POST['subject_name']
        ID = request.POST['subject_ID']
        credit = request.POST['subject_credit']            #display contents of subject
        program = request.POST['subject_program']
        program = Program.objects.get(name = program)
        subject_add(name, ID, program, credit)
    return render_to_response("subject.html", 
                                {"subject_list" : subject_list, 
                                    'program_list':program_list},
                                 RequestContext(request))

#Program page
def program_add(name, credit):
    """
    add a new program to database with:
    name : name of a program (string)
    credit : credit of a program (number)
    """
    new_program = Program()
    new_program.name = name
    new_program.credits = credit
    new_program.save()

def program(request):
    """
    program view for program url
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')                #if wrong user
    program_list = Program.objects.all()
    if request.POST:
        name = request.POST['program_name']
        credit = request.POST['program_credit']
        program_add(name, credit)
    return render_to_response("program.html",
                                {'program_list':program_list},
                                RequestContext(request))



def statistic(request):
    """
    handle view for statistic url (general site)
    """
    if not request.user.is_authenticated:            #if wrong user
        return HttpResponse('wrong')
    lecturer_list = Lecturer.objects.all()
    return render_to_response("statistic.html",
                                 {'lecturer_list': lecturer_list})

#statistic page for individual lecturer
def statistic_individual_lecturer(request, lecturer_name):
    """
    this funtion handle statistic view for a specific lecturer
    redirect from statistic view
    """
    if not request.user.is_authenticated:
        return HttpResponse('u need to login')
    lecturer_list = Lecturer.objects.all()
    #get Lecturer object with lecturer_name
    current_lecturer = Lecturer.objects.get(name = lecturer_name)
    lecturer_info = Lecturer_teaching_info.objects.get(lecturer__in = 
                                                        [current_lecturer,])
    credit_count = lecturer_info.credit
    return render_to_response("statistic_individual.html", 
                                {'lecturer_info':lecturer_info,
                                'lecturer_list':lecturer_list,
                                'credit_count':credit_count})
