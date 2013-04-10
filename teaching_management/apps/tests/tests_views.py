from django.test import TestCase
from apps.views import *
from apps.models import Program
class Test(TestCase):
	def test_adding_scheduler(self):
		scheduler_add('april')
		self.assertEqual(Scheduler.objects.count(), 1)
	
	def test_adding_lecturer(self):
		lecturer_add('truong anh hoang', 'IT', [], [], 20)
		self.assertEqual(Lecturer.objects.count(), 1)
		
# 	def test_adding_subject(self):
# 		subject_add('computer architecture', 'INT2025', Program(name='ISP', credits=152) , 4)
# 		self.assertEqual(Subject.objects.count(), 1)
