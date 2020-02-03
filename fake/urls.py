from django.conf.urls import url
from fake import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^table/$', views.table, name='table'),
    url(r'^list/$', views.lst, name='list'),
    url(r'^form/$', views.form, name='form'),
    url(r'^form2/$', views.form2, name='form2'),
]
