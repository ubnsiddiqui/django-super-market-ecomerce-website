from django.conf.urls import url

from . import views

app_name = 'super_market'

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^login/$', views.user_login, name='login'),
               url(r'^logout/$', views.user_logout, name='logout'),
               url(r'^register/$', views.register, name='register'),
               ]