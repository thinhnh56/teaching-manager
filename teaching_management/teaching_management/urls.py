from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.views import profile, scheduler_link, scheduler, lecturer, subject, program, statistic
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teaching_management.views.home', name='home'),
    # url(r'^teaching_management/', include('teaching_management.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^$', login),   	#link to login site
	(r'subject$', subject),   #link to subject site
	(r'lecturer$', lecturer),   #link to lecturer site
	(r'Program$', program),		#link to program site	
	(r'accounts/profile/$', profile),	
	(r'scheduler$', scheduler),	#link to scheduler site
	(r'scheduler/([A-Za-z]+[^/]+)$', scheduler_link),	#link to the scheduler of each content of schedule
	(r'statistic$', statistic),     	#link to statistic site
	(r'^home$',login),					#link to homepage (~ login site)
    url(r'^admin/', include(admin.site.urls)),  #link to admin site
)
