from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.views import profile, sheduler, lecturer, subject, program, statistic
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teaching_management.views.home', name='home'),
    # url(r'^teaching_management/', include('teaching_management.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^$', login),
	(r'^subject$', subject),
	(r'^lecturer$', lecturer),
	(r'^Program$', program),
	(r'^accounts/profile/$', profile),
	(r'^sheduler$', sheduler),
	(r'^statistic$', statistic),
    url(r'^admin/', include(admin.site.urls)),
)
