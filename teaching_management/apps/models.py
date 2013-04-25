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
    name = models.CharField(max_length = 30)
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
    name = models.CharField(max_length = 30)
    ID = models.CharField(max_length = 10, primary_key = True)
    program = models.ForeignKey(Program)
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
    name = models.CharField(max_length = 30)
    faculty = models.CharField(max_length = 50)
    subjects_in_charge = models.ManyToManyField(Subject, related_name = 'c+')
    subjects_can_teach = models.ManyToManyField(Subject, related_name = 't+')
    credits = models.IntegerField()
    def __unicode__(self):
        return self.name
    

class Scheduler(models.Model):
    """
    Scheduler field includes:
    Name of Scheduler
    """
    name = models.CharField(max_length = 30)
    
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
    scheduler = models.ForeignKey(Scheduler)
    subject = models.ForeignKey(Subject)
    lecturer = models.ManyToManyField(Lecturer)


class Lecturer_teaching_info(models.Model):
    """
    this model store infomation about
        subjects that Lecturer has taught
    """
    lecturer = models.ForeignKey(Lecturer)
    subject = models.ManyToManyField(Subject)
    credit = models.IntegerField()
    
    def update(self, subject):
        self.subject.add(subject)
        self.credit = self.credit + subject.credits
        self.save()
        
    def __unicode__(self):
        return self.lecturer.name