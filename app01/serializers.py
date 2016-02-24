#coding:utf-8
from rest_framework import serializers
from app01 import models
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['username','email']

      
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Host
        fields = ['id','name','description','ip','nationality',
                  'province','city','idc','flood',
                  'equipment','group','pull_interval',]
        
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Group
        field = ['name','description']

       
class TaskCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskCenter
        fields = ['id','name','description','task_type','host','group',
                  'content','created_by','kick_off_at']
        #depth = 3
        
class TaskLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TaskLog
        fields = ['task','result_status','result_log','client_info','date']