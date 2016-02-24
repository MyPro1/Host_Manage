#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,verbose_name=u'用户')
    email = models.EmailField()
    def __unicode__(self):
        return '%s' % self.user
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Host(models.Model):
    name = models.CharField(u'主机名',max_length=30)
    description = models.CharField(u'主机描述',max_length=300,null=True,blank=True)
    ip = models.IPAddressField(u'主机IP地址')
    nationality = models.CharField(u'主机所属国家',max_length=50,null=True,blank=True)
    province = models.CharField(u'主机所属省份',max_length=50,null=True,blank=True)
    city = models.CharField(u'主机所属城市',max_length=50,null=True,blank=True)
    idc = models.CharField(max_length=50,verbose_name=u'主机所属机房',null=True,blank=True)
    flood = models.CharField(max_length=50,verbose_name=u'主机所属楼层',null=True,blank=True)
    equipment = models.CharField(max_length=50,verbose_name=u'主机所属机柜',null=True,blank=True)
    group = models.ManyToManyField('Group',max_length=50,verbose_name=u'主机所属组')
    pull_interval = models.IntegerField(u'更新时间间隔',max_length=50)
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '主机名'
        verbose_name_plural = '主机名'
        
class Group(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'主机组名字')
    description = models.CharField(max_length=300,verbose_name=u'主机组描述',null=True,blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '主机组'
        verbose_name_plural = '主机组'
    
class TaskCenter(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'任务名称')
    description = models.CharField(max_length=300,verbose_name=u'任务描述')
    task_choice = (('cmd','命令执行'),
                 ('file_transfer','文件管理'),
                 ('config_manager','配置管理'),)
    
    task_type = models.CharField(choices=task_choice,verbose_name=u'任务类型',max_length=40)
    host = models.ManyToManyField('Host',verbose_name=u'任务主机',max_length=30)
    group = models.ManyToManyField('Group',verbose_name=u'任务主机组',max_length=30)
    content = models.CharField(u'任务内容',max_length=30)
    created_by= models.ForeignKey('UserProfile',verbose_name=u'任务创建者',blank=True,null=True)
    kick_off_at = models.DateTimeField(u'任务执行时间',blank=True,null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = '任务名'
        verbose_name_plural = '任务名'
    
class TaskLog(models.Model):
    task = models.ForeignKey('TaskCenter',verbose_name=u'任务日志')
    result_choices = (('success','成功'),
                     ('failed','失败'),
                     ('unknow','未知'),)
    result_status = models.CharField(choices=result_choices,verbose_name=u'结果类型',max_length=40)
    result_log = models.TextField(u'结果日志')
    client_info = models.TextField(u'客户端信息')
    date = models.DateTimeField(u'日志产生的日期',auto_now_add=True)
    
    def __unicode__(self):
        return self.task
    
    
    class Meta:
        verbose_name = '任务日志'
        verbose_name_plural = '任务日志'
