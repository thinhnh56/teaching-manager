from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from apps.models import *
class test(TestCase):
	def test_login(self):
		client = Client ()
		Credits_for_test = 3
		client.login(username='admin', password='mraisvip93')
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.program = Program()
		self.program.name = 'IS'
		self.program.credits = 152
		self.program.save()
		# self.assertEqual(self.program.name, 'ISP')
		client.post('/accounts/profile/subject',
 						{'subject_name': 'toan roi rac',
 						'subject_ID' : '11111',
 						'subject_credit' : Credits_for_test,
 						'subject_program' : 'IS'})
		client.post('/accounts/profile/subject',
 						{'subject_name': 'do hoa may tinh',
 						'subject_ID' : '22222',
 						'subject_credit' : Credits_for_test,
 						'subject_program' : 'IS'})
		client.post('/accounts/profile/subject',
 						{'subject_name': 'lap trinh nang cao',
 						'subject_ID' : '33333',
 						'subject_credit' : Credits_for_test,
 						'subject_program' : 'IS'})
		client.post('/accounts/profile/subject',
 						{'subject_name': 'tin hoc co so',
 						'subject_ID' : '44444',
 						'subject_credit' : Credits_for_test,
 						'subject_program' : 'IS'})
		
		dhmt = Subject.objects.get(name='do hoa may tinh')
		trr = Subject.objects.get(name='toan roi rac')
		ltnc = Subject.objects.get(name='lap trinh nang cao')
		thcs = Subject.objects.get(name='tin hoc co so')
		
		
		client.post('/accounts/profile/\lecturer',
					{'lecturer_name' : 'ngo le bao loc',
					'lecturer_falcuty' : 'cong nghe thong tin',
					'lecturer_credit' : Credits_for_test,
					'subjects_in_charge' : [dhmt],
					'subjects_can_teach' : [thcs, dhmt, trr]})
		client.post('/accounts/profile/\lecturer',
					{'lecturer_name' : 'nguyen hung thinh',
					'lecturer_falcuty' : 'cong nghe thong tin',
					'lecturer_credit' : Credits_for_test,
					'subjects_in_charge' : [trr, ltnc],
					'subjects_can_teach' : [trr, ltnc, thcs, dhmt]})
		
		self.assertEqual(response.status_code, 200)
		
		client.post('/scheduler/\scheduler',
				{'schedule_name' : 'first term'})
		self.assertEqual(response.status_code, 200)
		
		response = client.get('/statistic/nguyen hung thinh')
		self.assertContains(response, '6')
		
