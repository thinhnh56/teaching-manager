from django.test import TestCase
from apps.models import *
		
class TestTheModels(TestCase):
	def test_adding_program(self):
		"""test adding a program"""
		def setup(self):
			self.program = Program(name='ISP', credits=152)
		def test(self):
			self.assertEqual(self.program.name, 'ISP')
			self.assertEqual(self.program.credits, 152)
			
		
	def test_adding_Subject(self):
		def setup(self):
			"""adding a subject"""
			self.subject = Subject(name='SE', ID='INT1111', credits=3)
		
		def test(self):
			"""test asserting the subject's parameters"""
			self.assertEqual(self.subject.name, 'SE')
			self.assertEqual(self.subject.ID, 'INT1111')
			self.assertEqual(self.subject.credits, 3)
			
		
	def test_adding_lecturer(self):
		def setup(self):
			"""adding a lecturer"""
			self.lecturer = Lecturer(name='tuan anh', falcuty='IT')
			
		def test(self):
			"""test asserting lecturer's parameters"""
			self.assertEqual(self.lecturer.name, 'tuan anh')
			self.assertEqual(self.lecturer.falcuty, 'IT')
			
		
	def test_adding_scheduler(self):
		def setup(self):
			"""adding a scheduler"""
			self.scheduler = Scheduler(name='April')
			
		def test(self):
			"""asserting"""
			self.assertEqual(self.scheduler.name, 'April')
