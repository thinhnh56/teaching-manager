from django.db import models

class Lecturers(models.Model):
    idlecturers = models.IntegerField(primary_key=True) # Field name made lowercase.
    name = models.CharField(max_length=135) # Field name made lowercase.
    email = models.EmailField() # Field name made lowercase.
    def __unicode__(self):
        return self.name

class StudentGuiding(models.Model):
    guiding_id = models.CharField(max_length=30, primary_key=True) # Field renamed to remove spaces. Field name made lowercase.
    name = models.CharField(max_length = 30)
    number_of_student = models.IntegerField() # Field renamed to remove spaces. Field name made lowercase.
    credits = models.IntegerField()
    def __unicode__(self):
        return self.name

class Subjects(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=135)
    credits = models.IntegerField()
    #lecturers = models.ManyToManyField(Lecturers)
    def __unicode__(self):
        return self.name

class LecturersHasStudentGuiding(models.Model):
    lecturers_idlecturers = models.ForeignKey(Lecturers) # Field name made lowercase.
    student_guiding_guiding = models.ForeignKey(StudentGuiding) # Field renamed to remove spaces. Field name made lowercase

class LecturersHasSubjects(models.Model):
    lecturers_idlecturers = models.ForeignKey(Lecturers) # Field name made lowercase.
    subjects = models.ForeignKey( Subjects) # Field name made lowercase.


