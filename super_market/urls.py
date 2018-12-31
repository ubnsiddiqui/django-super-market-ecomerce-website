from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from mysite import settings
from . import views

app_name = 'super_market'

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^login/$', views.user_login, name='login'),
               url(r'^logout/$', views.user_logout, name='logout'),
               url(r'^register/$', views.register, name='register'),
               url(r'^contact/$', views.contact, name='contact'),
               url(r'^products/$', views.display_products, name='product'),
               url(r'^checkout/$', views.checkout, name='checkout'),
               url(r'^single-item-description/(?P<product>\d+)/$', views.single, name='single'),
               ]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)