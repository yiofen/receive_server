from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index1, name='index1'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^savefile/$', views.save_file, name='save_file'),
    url(r'^retdata/$', views.ret_data, name='ret_data')
]
