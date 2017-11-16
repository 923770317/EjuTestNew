from django.conf.urls import url

import views
import view_if

urlpatterns = [url(r'^release/$', views.releaseIndex),
                url(r'^productSites/$', views.productSites),
                url(r'^$', views.index),
                url(r'^tools/deletePassWord/$', views.deletePassWord),
                url(r'^tools/deleteCert/$', views.deleteCert),
                url(r'^tools/deletePass/$', views.deletePassWord),
                url(r'^tools/updateAccount/$', views.updateAccount),
                url(r'^tools/updateReceiptAmount/$', views.updateReceiptAmount),
                url(r'^tools/interfaceGrant/$', views.interfaceGrant),
               url(r'^tools/sendRequest/$', views.sendRequest),
               url(r'^api/getOptions/$', view_if.getOption),]
