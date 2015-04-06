from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'emailApp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^refresh/', 'emailApp.views.refresh', name = 'refresh'),
    url(r'^save/', 'emailApp.views.saveAllUnreadEmails', name = 'save'),
    url(r'fetch/','emailApp.views.fetchAllUnreadEmails',name='fetch'),
    url(r'clean/','emailApp.views.cleanText',name='clean'),
    url(r'labels/','emailApp.views.updateLables',name='labels'),
    url(r'dashboard/','emailApp.views.dashboard',name='dashboard'),
    url(r'^(?P<messageId>[-\w]+)/$', 'emailApp.views.messagePage', name='messagePage'),

)
