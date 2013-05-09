""""
View handle request from user
and display response
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.models import *

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
        #lecturer's name
        current_lecturer = Lecturer_teaching_info.objects.get(lecturer__in = [lecturer,])
        current_lecturer.update(subject)
    except Lecturer_teaching_info.DoesNotExist :
        new_lecturer = Lecturer_teaching_info()
        #initiate new_lecturer
        new_lecturer.credit = 0
        new_lecturer.lecturer = lecturer
        new_lecturer.save()
        new_lecturer.update(subject)
        new_lecturer.save()
        
        
#add scheduler_link function
def add_scheduler_link(given_scheduler, given_subject, lecturer_list):
    """
    add a scheduler_link to database
    (link scheduler, subject and a list of lecturers)
    """
    
    new_scheduler_link = Scheduler_link() #initiation
    
    #add contents of schuedule link
    new_scheduler_link.scheduler = given_scheduler
    new_scheduler_link.subject = given_subject
    new_scheduler_link.save()
    
    # link lecturer in given lecturer_list to given subject                    
    for given_lecturer in lecturer_list:
        new_scheduler_link.lecturer.add(given_lecturer)
        #every time assign subject to a lecturer we wil update that lecturer's teaching infomation
        update_lecturer_teaching_info(given_lecturer, given_subject)
        
    new_scheduler_link.save()

#link scheduler info to
def scheduler_link(request, given_schedule_name):
    """"
    display for specific scheduler page, and handle information posted by user
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')                #if wrong user
    
    
    
    if request.POST:
        # we have two form in our page so we classify which form is sending
        # request by examine 'form_type'
        if request.POST['form_type'] == 'new_schedule' :
            schedule_name = request.POST['schedule_name']
            scheduler_add(schedule_name)
                                   
        elif request.POST['form_type'] == 'add_link':
            #current_schedule_name is the name of the schedule we are viewing
            current_schedule_name = given_schedule_name
            current_scheduler = Scheduler.objects.get(name = current_schedule_name)
            #get subject_ID through post form and turn it to Subject object          
            posted_subject_ID = request.POST['subject_ID']                        
            posted_subject = Subject.objects.get(ID = posted_subject_ID)
            #post data for lecturers is a list, and we store in posted_lecturer_list 
            posted_lecturer_list = request.POST.getlist('lecturers')
            #posted_lecturer_list currently a list of lecturer name(a string)
            #so we convert it to Lecturer objects
            #we use a temp list to store converted lecturer object
            temp_list = []
            for lecturer_name in posted_lecturer_list :
                temp_list.append(Lecturer.objects.get(name = lecturer_name))
            # posted_lecturer_list now become a list of Lecturer object
            posted_lecturer_list = temp_list
            
            add_scheduler_link(current_scheduler, posted_subject, posted_lecturer_list)
            
    #these variables support infomation for display page
    schedule_list = Scheduler.objects.all()
    lecturer_list = Lecturer.objects.all()
    subject_list = Subject.objects.all()
    """
       there exist a lot of scheduler_link in database 
       we get a list of scheduler_link with given_schedule name  
    """
    scheduler_link_list = Scheduler_link.objects.filter(
                            scheduler__in = 
                            [Scheduler.objects.get(name = given_schedule_name),])
    return render_to_response("schedule_list.html", 
                                {'lecturer_list':lecturer_list, 
                                'subject_list':subject_list, 
                                'schedule_list':schedule_list, 
                                'schedule_name':given_schedule_name, 
                                'scheduler_link_list':scheduler_link_list},
                                RequestContext(request))
#scheduler page
def scheduler(request):
    """
    scheduler view for scheduler page
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')            #if wrong url
    
    scheduler_list = Scheduler.objects.all()
    
    if request.POST:
        scheduler_name = request.POST['schedule_name']
        scheduler_add(scheduler_name)
    
    return render_to_response("scheduler.html", 
                                {'schedule_list':scheduler_list}, 
                                RequestContext(request))
#add schedule function
def scheduler_add(given_name):
    """
    add new scheduler
    """
    new_scheduler = Scheduler()
    new_scheduler.name = given_name
    new_scheduler.save()


#Home page
def home (request):
    if not request.user.is_authenticated:
        return HttpResponse('wrong')
    return render_to_response ("home.html")

#add new lecturer function
def lecturer_add(given_name, given_faculty, 
                 given_subjects_in_charge, 
                 given_subjects_can_teach, 
                 given_credit):
    """
    add a new lecturer to database:
    given_name : given_name of a lecturer (string)
    given_faculty : given_name of lecturer's given_faculty
    given_subjects_in_charge : a list of subject object
    given_subjects_can_teach : a list of subject object
    given_credit: amount of credits assigned to lecturer (number)
    """
    new_lecturer = Lecturer()
    new_lecturer.name = given_name
    #add contents of lecturer
    new_lecturer.faculty = given_faculty 
    new_lecturer.credits = given_credit
    new_lecturer.save()
    
    for subject in given_subjects_in_charge:
        new_lecturer.subjects_in_charge.add(subject)        
    
    for subject in given_subjects_can_teach:
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
        #get post data from user, all of them are strings not objects
        faculty = request.POST['lecturer_faculty']                        
        credit = request.POST['lecturer_credit']
        subjects_in_charge = request.POST.getlist('subjects_in_charge')
        subjects_can_teach = request.POST.getlist('subjects_can_teach')
        #convert subjects_in_charge to a list of Subjects
        #temp list to store converted Subject objects
        temp_list = []
        for subject in subjects_in_charge:
            temp_list.append(Subject.objects.get(name = subject))
        subjects_in_charge = []
        subjects_in_charge = temp_list
        # similar to subjects_in_charge                                
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
def subject_add(given_name, given_ID, given_program, given_credit):
    """
    add new subject to database with:
    given_name : given_name of a subject ( string )
    given_ID : identifier of a subject (string)
    given_program : exist given_program object in databse (Program object)
    creidt : given_credit of a subject  (number)
    """
    new_subject = Subject()
    new_subject.name = given_name                    #add contents of subject
    new_subject.ID = given_ID
    new_subject.program = given_program
    new_subject.credits = given_credit
    new_subject.save()

#subject pageh
def subject(request):
    """
    function display for subject page
    """
    if not request.user.is_authenticated:
        return HttpResponse('wrong')            #if wrong user
        
    if request.POST:                            
        name = request.POST['subject_name']
        ID = request.POST['subject_ID']
        credit = request.POST['subject_credit']            #display contents of subject
        program = request.POST['subject_program']
        program = Program.objects.get(name = program)
        subject_add(name, ID, program, credit)
        
    subject_list = Subject.objects.all()
    program_list = Program.objects.all()
    return render_to_response("subject.html", 
                                {"subject_list" :subject_list, 
                                 "program_list":program_list},
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
    #
    try :
        current_lecturer_info = Lecturer_teaching_info.objects.get(lecturer__in = 
                                                        [current_lecturer,])
        credit_count = current_lecturer_info.credit
        lecturer_info = current_lecturer_info
    
    except Lecturer_teaching_info.DoesNotExist :
        new_lecturer_info = Lecturer_teaching_info()
        new_lecturer_info.credit = 0
        new_lecturer_info.lecturer = current_lecturer
        new_lecturer_info.save()
        
        lecturer_info = new_lecturer_info
        credit_count = lecturer_info.credit
        
    return render_to_response("statistic_individual.html", 
                                {'lecturer_info':lecturer_info,
                                'lecturer_list':lecturer_list,
                                'credit_count':credit_count})
