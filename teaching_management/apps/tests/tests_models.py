"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from apps.models import *

# class SimpleTest(TestCase):
# 	def test_basic_addition(self):
# 		"""
# 		Tests that 1 + 1 always equals 2.
# 		"""
# 		self.assertEqual(1 + 1, 2)
		
class TestTheModels(TestCase):
	def test_adding_program(self):
		def setup(self):
			self.program = Program(name='ISP', credits=152)
		def test(self):
			self.assertEqual(self.program.name, 'ISP')
			self.assertEqual(self.program.credits, 152)
			
		
	def test_adding_Subject(self):
		def setup(self):
			self.subject = Subject(name='SE', ID='INT1111', credits=3)
		
		def test(self):
			self.assertEqual(self.subject.name, 'SE')
			self.assertEqual(self.subject.ID, 'INT1111')
			self.assertEqual(self.subject.credits, 3)
			
		
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
