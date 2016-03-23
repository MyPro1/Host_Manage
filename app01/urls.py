#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import viewsets,serializers,routers
from app01 import views

router = routers.DefaultRouter()
router.register(r'UserProfile',views.UserProfileViewSet)
router.register(r'Host', views.HostViewSet)
router.register(r'Group',views.GroupViewSet)
router.register(r'TaskCenter',views.TaskCenterViewSet)
router.register(r'TaskLog',views.TaskLogViewSet)

urlpatterns = patterns('',
    url(r'^',include(router.urls)),
    url(r'^base/$',views.base),
    url(r'^task_center/$',views.task_center),
    url(r'^new_task/$',views.new_task),
    #url(r'^new_tasks/(?P<last_task_id>\d+)/$',views.new_tasks),
    url(r'^hostconf/(?P<host_id>\d+)/$',views.HostConf),
    url(r'^taskconf/(?P<task_id>\d+)/$',views.TaskConf),
    url(r'^task_result/(?P<task_result_id>\d+)/$',views.task_result),
    url(r'^task_detail/(?P<task_detail_id>\d+)/$',views.task_detail),
    url(r'^index/$',views.index),
)

