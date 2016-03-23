#coding:utf-8
from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponseRedirect
from app01 import serializers
from app01 import models
from rest_framework import viewsets
from app01 import custform
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    

class HostViewSet(viewsets.ModelViewSet):
    queryset = models.Host.objects.all()
    serializer_class = serializers.HostSerializer
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    
class TaskCenterViewSet(viewsets.ModelViewSet):
    queryset = models.TaskCenter.objects.all()
    serializer_class = serializers.TaskCenterSerializer

class TaskLogViewSet(viewsets.ModelViewSet):
    queryset = models.TaskLog.objects.all()
    serializer_class = serializers.TaskLogSerializer
    

def base(request):
    return render_to_response('base.html')

def task_center(request):
    task_list = []
    task_info = {}
    form = custform.TaskCenterForm()
    for task in models.TaskCenter.objects.all():
        task_info = {
            'id':task.id,
            'name':task.name,
            'description':task.description,
            'type':task.task_type,
            'content':task.content,
            'created_by':task.created_by,
            'kick_off_at':task.kick_off_at,
            'host_count':models.TaskLog.objects.filter(task_id=task.id).count(),
            'failure':models.TaskLog.objects.filter(task_id=task.id,result_status=1).count(),
            'success':models.TaskLog.objects.filter(task_id=task.id,result_status=0).count(),
            
                     }
        
        print task_info['failure']
        print task_info['success']
        print task_info['id']
    #print task_info
        task_list.append(task_info)
    #print task_list
    return render_to_response('task_center.html',{'form':form,'task_list':task_list})
    
@api_view(['POST'])
def new_task(request):
    form = custform.TaskCenterForm(request.POST)
    if form.is_valid():
        #data = form.cleaned_data
        form.save()
        return HttpResponseRedirect('/api/task_center/')
    else:
        print form.errors
        return render_to_response('task_center.html',{'form':form})
        
"""
@api_view(['GET'])
def new_tasks(request,last_task_id):
        
    query_set = models.TaskCenter.objects.filter(id__gt=last_task_id)
    serializer_class = serializers.TaskCenterSerializer(query_set,many=True)
    return Response(serializer_class.data)
"""

@api_view(['GET'])
def HostConf(request,host_id):
    queryset = models.Host.objects.get(id=host_id)
    print '----------' ,queryset
    serializer_data = serializers.HostSerializer(queryset)
    print '--------------->serializer_data',serializer_data
    return Response(serializer_data.data)

@api_view(['GET'])
def TaskConf(request,task_id):
    queryset_task = models.TaskCenter.objects.filter(id__gt=task_id)
    serializer_data_task = serializers.TaskCenterSerializer(queryset_task,many=True)
    #print serializer_data_task
    return Response(serializer_data_task.data)


@api_view(['POST'])
def task_result(request,task_result_id):
    host_profile = request.data['host_profile']
    host_profile = json.loads(host_profile)
    #print type(host_profile)
    task_profile = json.loads(request.data['task_center'])
    task_obj = models.TaskCenter.objects.get(id=task_profile.get('id'))
    #print task_obj
    result_status = request.data['self.result_type']
    result_data = request.data['self.result_data']
    #print result_type,result_data,host_profile
    models.TaskLog.objects.create(task=task_obj,
                                  result_status = result_status,
                                  result_log = result_data,
                                  client_info = host_profile['ip'])
    return HttpResponse('Submit success')

def task_detail(request,task_detail_id):
    task_dic = {}
    task_list = []
    for log in models.TaskLog.objects.filter(task_id=task_detail_id):
        #host = models.Host.objects.get(id=task_detail_id)
        #log.client_info
        task_dic = {
                    'date':log.date,
                    'client':log.client_info,
                    'result_status':log.result_status,
                    'result_data':log.result_log,
                    }
        task_list.append(task_dic)
    #print task_detail
    return HttpResponse(task_list)
    #return render_to_response('task_detail.html')

def index(request):
    return render_to_response('index.html')





