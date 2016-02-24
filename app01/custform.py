#coding:utf-8
from django.forms import ModelForm
from app01 import models
from django import forms
class TaskCenterForm(ModelForm):
    class Meta:
        model = models.TaskCenter
        fields = ['name','description','task_type','host','group','content',
                 'created_by','kick_off_at',]
       
    def __init__(self,*args,**kargs):
        super(TaskCenterForm,self).__init__(*args,**kargs)
        self.fields['host'].widget.attrs.update({'class': 'form-control'})
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['task_type'].widget.attrs.update({'class':'form-control'})
        self.fields['group'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['created_by'].widget.attrs.update({'class': 'form-control'})
        self.fields['kick_off_at'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})