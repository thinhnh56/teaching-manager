"""
act as a client, post data to website and wait for response
"""
from django.test import TestCase
from django.test.client import Client
from apps.models import *

class test_statistic(TestCase):
	def test(self):
		self.client = Client()

		#add a new program to database
		program = Program()
		program.name = 'IS'
		program.credits = 152
		program.save()
		
		#add new subject
		test_subject_name = 'do hoa may tinh'
		test_subject_ID = '22222'
		test_subject_credit = 3
		test_subject_program = 'IS'
		add_subject_url  ='/accounts/profile/subject' 
		self.client.post(add_subject_url,
 					{'subject_name': test_subject_name,
 					'subject_ID' : test_subject_ID,
 					'subject_credit' : test_subject_credit,
 					'subject_program' : test_subject_program})
		test_subject = Subject.objects.get(name = test_subject_name)
		
		# add new lecturer to database
		test_lecturer_name = 'ngo le bao loc'
		test_lecturer_faculty = 'cong nghe thong tin'
		test_lecturer_credit = 20
		test_lecturer_subject_in_charge = [test_subject,]
		test_lecturer_subject_can_teach = [test_subject,] 
		add_lecturer_url = '/accounts/profile/\lecturer' 
		
		self.client.post(add_lecturer_url,
					{'lecturer_name' : test_lecturer_name,
					'lecturer_faculty' : test_lecturer_faculty,	
					'lecturer_credit' : test_lecturer_credit,
					'subjects_in_charge' : test_lecturer_subject_in_charge,
					'subjects_can_teach' : test_lecturer_subject_can_teach})
		
		test_lecturer = Lecturer.objects.get(name = test_lecturer_name)
		# add new schedule
		test_schedule_name = 'first term'
		add_schedule_url = '/accounts/profile/\scheduler'
		self.client.post(add_schedule_url,
				{'schedule_name' : test_schedule_name})
		
		# assign subject to lecturer
		add_link = 'add_link'
		add_schedule_link_url = '/scheduler/'+test_schedule_name 
		self.client.post(add_schedule_link_url,
				{'form_type' : add_link,
				'subject_ID' : test_subject_ID,
				'lecturers' : test_lecturer.name})

		column_contain_lecturer_credit = '<td>3</td>'
		response_url = '/statistic/' + test_lecturer.name
		htmlres = self.client.get(response_url)
		self.assertContains(htmlres, column_contain_lecturer_credit)
		
