from django.conf.urls import url
from .views import (posts_home, post_create, post_delete, post_detail, post_modify, add_comment, attend, register)
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView



urlpatterns = [
    url(r'^$', posts_home, name="home"),
    url(r'^create/$', post_create, name="post_create"),

    # Django provides login and logout views so we only need the templates
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}),

    # For registering a new user
    url(r'^register/$', register, name='register'),

    # After logging in it redirects to accounts/profile so we redirect to homepage
    url(r'^accounts/profile/$', RedirectView.as_view(pattern_name='index')),

    
    url(r'^(?P<slug>[\w\-]+)/$', post_detail, name="post_detail"),
    url(r'^(?P<slug>[\w\-]+)/modify/$', post_modify, name="post_modify"),
    url(r'^(?P<slug>[\w\-]+)/delete/$', post_delete, name="post_delete"),
    url(r'^(?P<slug>[\w\-]+)/comment/$', add_comment, name="add_comment"),
    url(r'^(?P<slug>[\w\-]+)/attend/$', attend, name="attend"),
]
