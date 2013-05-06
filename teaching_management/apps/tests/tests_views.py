
"""
test for funtions implemented in views 
"""
from django.test import TestCase
from apps.views import *
from     apps.models import Program
class Test(TestCase):
    def test_adding_scheduler(self):
        def setup(self):
            self.new_schedule_name = 'april'
        def test():
            before_add_count = Scheduler.objects.count()
            scheduler_add(self.new_schedule_name)
            after_add_count = before_add_count
            self.assertEqual(Scheduler.objects.count(), after_add_count)
    


    def test_adding_lecturer(self):
        def setup(self):
            self.lecturer_name = 'truong anh hoang'
            self.lecturer_faculty = 'ID'
            self.subject_in_charge_list = []
            self.subject_can_teach_list = []
            self.lecturer_credits = 20
        def test():
            before_add_count = Lecturer.objects.count()
            lecturer_add(self.lecturer_name, self.lecturer_faculty, 
                        self.subject_in_charge_list, 
                        self.subject_can_teach_list, self.lecturer_credits)
            after_add_count = before_add_count + 1;
            self.assertEqual(Lecturer.objects.count(), after_add_count)
            
    def test_program_add(self):
        def setup(self):
            self.new_program_name = 'ISP'
            self.new_program_credits = 152
        def test(self):
            before_add_count = Program.objects.count()
            program_add(self.new_program_name, self.new_program.credits)
            after_add_count = before_add_count + 1
            self.assertEqual(Program.objects.count(), after_add_count)
            
    def test_adding_subject(self):
        def setup():
            new_program_name = 'ISP'
            new_program_credits = 152
            self.new_program = Program()
            self.new_program.name = new_program_name
            self.new_program.credits = new_program_credits
            self.new_program.save()
            
            self.new_subject_name = 'computer architecture'
            self.new_subject_ID = 'INT 2025'
            self.new_subject_credits = 4
        def test():
            before_add_count = Subject.objects.count() 
            subject_add(self.new_subject_name, self.new_subject_ID, 
                        self.new_program , self.new_subject_credits)
            after_add_count = before_add_count + 1
            self.assertEqual(Subject.objects.count(), after_add_count)
