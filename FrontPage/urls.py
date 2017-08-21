from django.conf.urls import url

import views

urlpatterns = [ url(r'^release/$', views.releaseIndex),
                url(r'^$', views.index),
                url(r'^tools/deletePassWord/$', views.deletePassWord),
                url(r'^tools/deleteCert/$', views.deleteCert),]