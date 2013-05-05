from django.test import TestCase
from apps.views import *
from apps.models import Program
class Test(TestCase):
	def test_adding_scheduler(self):
		"""test adding a scheduler named "april""""
		scheduler_add('april')
		self.assertEqual(Scheduler.objects.count(), 1)
	
	def test_adding_lecturer(self):
		"""test adding a lecturer named "Lecturer test name""""
		lecturer_add('Lecturer test name', 'IT', [], [], 20)
		self.assertEqual(Lecturer.objects.count(), 1)
		
