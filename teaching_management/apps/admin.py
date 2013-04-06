from django.contrib import admin
from apps.models import Program, Subject, Lecturer, Scheduler, Scheduler_link

admin.site.register(Program)
admin.site.register(Subject)
admin.site.register(Lecturer)
admin.site.register(Scheduler)
admin.site.register(Scheduler_link)
