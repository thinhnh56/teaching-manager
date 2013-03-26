from django.conf.urls.defaults import patterns, include, url
from teaching_management.non_staff_user.views import nonStaffLogin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', nonStaffLogin),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
