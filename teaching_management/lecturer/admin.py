from django.contrib import admin
from teaching_management.lecturer.models import Lecturers, StudentGuiding, Subjects, LecturersHasStudentGuiding, LecturersHasSubjects

admin.site.register(Lecturers)
admin.site.register(StudentGuiding)
admin.site.register(Subjects)
admin.site.register(LecturersHasStudentGuiding)
admin.site.register(LecturersHasSubjects)