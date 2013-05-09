"""
    this file define models for database
"""
from django.db import models


class Program(models.Model):
    """
       program model contain imfomation about a program:
       name : name of a program
       credit: amount of credit that assigned to a program   
    """
    MAX_LENGTH = 30
    
    name = models.CharField(max_length = MAX_LENGTH)
    credits = models.IntegerField()
     
    def __unicode__(self):
        return self.name

    

class Subject(models.Model):
    """Subject field includes :
    Name of subject
    ID of subject
    Program which subject belong to
    Number of credits
    """
    NAME_MAX_LENGTH = 30
    ID_MAX_LENGTH = 10
    LINK_BACK_NAME = 'subject'
    
    name = models.CharField(max_length = NAME_MAX_LENGTH)
    ID = models.CharField(max_length = ID_MAX_LENGTH, primary_key = True)
    program = models.ForeignKey(Program, related_name = LINK_BACK_NAME)
    credits = models.IntegerField()
    
    def __unicode__(self):
        return self.name


class Lecturer(models.Model):
    """
    Lecturer field includes :
    Name of lecturer
    Faculty where Lecturers are working
    Subjects which a lecturer    are teaching
    Another Subjects which a lecturer can teach
    Number of credits that lecturer are teaching
    """
    NAME_MAX_LENGTH = 30
    FACULTY_MAX_LENGTH = 50
    #CHARGE_LINK_BACK is a name, which allow subject_in_charge to link back to lecturer
    #similarly with subjects_can_teach
    CHARGE_LINK_BACK = 'lecturer_in_charge'
    TEACH_LINK_BACK = 'lecturer_can_teach'
    name = models.CharField(max_length = NAME_MAX_LENGTH)
    faculty = models.CharField(max_length = FACULTY_MAX_LENGTH)
    subjects_in_charge = models.ManyToManyField(Subject, 
                                                related_name = CHARGE_LINK_BACK)
    subjects_can_teach = models.ManyToManyField(Subject, 
                                                related_name = TEACH_LINK_BACK)
    credits = models.IntegerField()
    def __unicode__(self):
        return self.name
    

class Scheduler(models.Model):
    """
    Scheduler field includes:
    Name of Scheduler
    """
    MAX_LENGTH = 30
    name = models.CharField(max_length = MAX_LENGTH)
    
    def __unicode__(self):
        return self.name

class Scheduler_link(models.Model):
    """
    Scheduler_link field includes:
    scheduler id
    subject
    lecturer
    model to connet
    """
    # this following variable represent objects Scheduler_link linked with 
    # specific objects type
    SCHEDULER_LINK_BACK = SUBJECT_LINK_BACK = LECTURER_LINK_BACK = 'scheduler_link'
    scheduler = models.ForeignKey(Scheduler, related_name = SCHEDULER_LINK_BACK)
    subject = models.ForeignKey(Subject, related_name = SUBJECT_LINK_BACK)
    lecturer = models.ManyToManyField(Lecturer, related_name = LECTURER_LINK_BACK)


class Lecturer_teaching_info(models.Model):
    """
    this model store infomation about
        subjects that Lecturer has taught
    """
    LECTURER_LINK_BACK = 'teaching_info'
    lecturer = models.ForeignKey(Lecturer, related_name = LECTURER_LINK_BACK)
    subject = models.ManyToManyField(Subject)
    credit = models.IntegerField()

    def __unicode__(self):
        return self.lecturer.name


    def update(self, given_subject):
        self.subject.add(given_subject)
        self.credit = self.credit + given_subject.credits
        self.save()
        