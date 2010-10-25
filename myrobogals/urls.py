from django.conf.urls.defaults import *
from myrobogals import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'rgmain.views.home'),
	(r'^welcome/(?P<chapterurl>.+)/$', 'rgmain.views.welcome'),
	(r'^login/$', 'rgprofile.views.show_login'),
	(r'^login/process/$', 'rgprofile.views.process_login'),
	(r'^logout/$', 'auth.views.logout', {'next_page': '/'}),
	(r'^chpass/$', 'auth.views.password_change', {'post_change_redirect': '/chpass/done/', 'template_name': 'password_change_form.html'}),
	(r'^chpass/done/$', 'rgprofile.views.password_change_done'),
	(r'^join/$', 'rgchapter.views.joinlist'),
	(r'^join/(?P<chapterurl>.+)/$', 'rgprofile.views.joinchapter'),
	(r'^profile/$', 'rgprofile.views.redirtoself'),
	(r'^profile/edit/$', 'rgprofile.views.redirtoeditself'),
	#(r'^profile/(?P<username>.+)/edit/profileimage/$', 'profileimages.views.upload_profile_image'),
	(r'^profile/(?P<username>.+)/edit/$', 'rgprofile.views.edituser'),
	(r'^profile/(?P<username>.+)/$', 'rgprofile.views.detail'),
	(r'^chapters/$', 'rgchapter.views.list'),
	(r'^chapters/my/$', 'rgchapter.views.redirtomy'),
	(r'^chapters/(?P<chapterurl>.+)/lists/(?P<list_id>\d+)/edit/$', 'rgprofile.views.edituserlist'),
	(r'^chapters/(?P<chapterurl>.+)/lists/(?P<list_id>\d+)/$', 'rgprofile.views.viewlist'),
	(r'^chapters/(?P<chapterurl>.+)/lists/add/$', 'rgprofile.views.adduserlist'),
	(r'^chapters/(?P<chapterurl>.+)/lists/$', 'rgprofile.views.listuserlists'),
	(r'^chapters/(?P<chapterurl>.+)/edit/users/add/$', 'rgprofile.views.adduser'),
	(r'^chapters/(?P<chapterurl>.+)/edit/users/$', 'rgprofile.views.editusers'),
	(r'^chapters/(?P<chapterurl>.+)/edit/$', 'rgchapter.views.editchapter'),
	(r'^chapters/(?P<chapterurl>.+)/join/$', 'rgprofile.views.joinchapter'),
	(r'^chapters/(?P<chapterurl>.+)/$', 'rgchapter.views.detail'),
	(r'^teaching/$', 'rgteaching.views.teachhome'),
	#(r'^teaching/availability/$', 'rgteaching.views.availability'),
	#(r'^teaching/training/$', 'rgteaching.views.training'),
	(r'^teaching/list/$', 'rgteaching.views.listvisits'),
	(r'^teaching/(?P<visit_id>\d+)/$', 'rgteaching.views.viewvisit'),
	(r'^teaching/(?P<visit_id>\d+)/invite/$', 'rgteaching.views.invitetovisit'),
	(r'^teaching/(?P<visit_id>\d+)/edit/$', 'rgteaching.views.editvisit'),
	(r'^teaching/(?P<event_id>\d+)/rsvp/(?P<user_id>\d+)/yes/$', 'rgteaching.views.rsvpyes'),
	(r'^teaching/(?P<event_id>\d+)/rsvp/(?P<user_id>\d+)/no/$', 'rgteaching.views.rsvpno'),
	(r'^teaching/(?P<event_id>\d+)/rsvp/(?P<user_id>\d+)/remove/$', 'rgteaching.views.rsvpremove'),
	(r'^teaching/schools/$', 'rgteaching.views.listschools'),
	(r'^teaching/schools/(?P<school_id>\d+)/$', 'rgteaching.views.editschool'),
	(r'^teaching/schools/new/$', 'rgteaching.views.newschool'),
	(r'^teaching/new/$', 'rgteaching.views.newvisit'),
	(r'^messages/$', 'rgmessages.views.list'),
	(r'^messages/(?P<msgid>\d+)/$', 'rgmessages.views.view'),
	(r'^messages/new/$', 'rgmessages.views.createnew'),
	(r'^messages/sms/write/$', 'rgmessages.views.writesms'),
	(r'^messages/sms/confirm/$', 'rgmessages.views.confirmsms'),
	(r'^messages/email/write/$', 'rgmessages.views.writeemail'),
	(r'^messages/email/done/$', 'rgmessages.views.emaildone'),
	(r'^messages/history/$', 'rgmessages.views.msghistory'),
	(r'^credits/$', 'rgmain.views.credits'),
	(r'^support/$', 'rgmain.views.support'),
	(r'^files/$', 'rgmain.views.files'),
	(r'^api/newsletter/$', 'rgmessages.views.api'),
	(r'^i18n/', include('django.conf.urls.i18n')),
	(r'^topsecretarea/', include(admin.site.urls)),
)
