"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

"""
test is provided for Models testing
so we use simple initiation to test
"""
from django.test import TestCase
from apps.models import *

class TestModels(TestCase):
	def test_adding_program(self):
		def setup(self):
			self.program = Program(name='ISP', credits=152)
		def test(self):
			self.assertEqual(self.program.name, 'ISP')
			self.assertEqual(self.program.credits, 152)
			
		
	def test_adding_Subject(self):
		def setup(self):
			#create new Subject object
			self.subject = Subject(name='SE', ID='INT1111', credits=3)
			self.trueName = 'SE'
			self.trueID = 'INT1111'
			self.trueCredits = 3
		def test(self):
			self.assertEqual(self.subject.name, self.trueName)
			self.assertEqual(self.subject.ID, self.trueID)
			self.assertEqual(self.subject.credits, self.trueCredits)
			
		
	def test_adding_lecturer(self):
		def setup(self):
			self.lecturer = Lecturer(name='tuan anh', falcuty='IT')
			
		def test(self):
			self.assertEqual(self.lecturer.name, 'tuan anh')
			self.assertEqual(self.lecturer.falcuty, 'IT')
			
		
	def test_adding_scheduler(self):
		def setup(self):
			self.scheduler = Scheduler(name='April')
			
		def test(self):
			self.assertEqual(self.scheduler.name, 'April')
