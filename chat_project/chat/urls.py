from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^registration/$', views.register, name='registration'),
    url(r'^chat/(?P<pk>\d+)/$', views.chat_page, name='chat_page'),
    url(r'^$', views.chat_list, name='chat_list'),
]
