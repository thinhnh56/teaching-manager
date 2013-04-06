from django.db import models

# Create your models here.

		
class Program(models.Model):
	name = models.CharField(max_length = 30)
	credit = models.IntegerField()
	
	def __unicode__(self):
		return self.name
		
class Subject(models.Model):
	name = models.CharField(max_length = 30)
	ID = models.CharField(max_length = 10, primary_key = True)
	program = models.ForeignKey(Program)
	credit = models.IntegerField()
	
	def __unicode__(self):
		return self.name

class Lecturer(models.Model):
	name = models.CharField(max_length = 30)
	falcuty = models.CharField(max_length = 50)
	subjects_in_charge = models.ManyToManyField(Subject, related_name = 'c+')
	subjects_can_teach = models.ManyToManyField(Subject, related_name = 't+')
	credit = models.IntegerField()
	def __unicode__(self):
		return self.name

class Scheduler(models.Model):
	name = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.name

class Scheduler_link(models.Model):
	scheduler = models.ForeignKey(Scheduler)
	subject = models.ForeignKey(Subject)
	lecturer = models.ManyToManyField(Lecturer)

	def __unicode__(self):
		return self.name
