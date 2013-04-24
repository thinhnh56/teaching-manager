from django.db import models

# Create your models here.

		
class Program(models.Model):
	name = models.CharField(max_length = 30)
	credits = models.IntegerField()
	
	def __unicode__(self):
                return self.name

	
#Subject field includes :
##Name of subject
##ID of subject
##Program which subject belong to
##Number of credits
 
class Subject(models.Model):
	name = models.CharField(max_length = 30)
	ID = models.CharField(max_length = 10, primary_key = True)
	program = models.ForeignKey(Program)
	credits = models.IntegerField()
	
	def __unicode__(self):
		return self.name

#Lecturer field includes :
##Name of lecturer
##Faculty where Lecturers are working
##Subjects which a lecturer	are teaching
##Another Subjects which a lecturer can teach
##Number of credits that lecturer are teaching
class Lecturer(models.Model):
	name = models.CharField(max_length = 30)
	falcuty = models.CharField(max_length = 50)
	subjects_in_charge = models.ManyToManyField(Subject, related_name = 'c+')
	subjects_can_teach = models.ManyToManyField(Subject, related_name = 't+')
	credits = models.IntegerField()
	def __unicode__(self):
		return self.name

#Scheduler field includes:
##Name of Scheduler
class Scheduler(models.Model):
	name = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.name

#Scheduler_link field includes:
##scheduler id
##subject
##lecturer
##model to connet
class Scheduler_link(models.Model):
	scheduler = models.ForeignKey(Scheduler)
	subject = models.ForeignKey(Subject)
	lecturer = models.ManyToManyField(Lecturer)
