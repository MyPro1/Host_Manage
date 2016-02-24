from django.contrib import admin
from app01 import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','email']
    
class HostAdmin(admin.ModelAdmin):
    list_display = ['name','description','ip','nationality',
                    'province','city','idc','flood',
                    'equipment','pull_interval']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    
class TaskCenterAadmin(admin.ModelAdmin):
    list_display = ['name','description','task_type',
                    'content','created_by','kick_off_at']
    
class TaskLogAdmin(admin.ModelAdmin):
    list_display = ['task','result_status','result_log','date']
    
admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.Host,HostAdmin)
admin.site.register(models.Group,GroupAdmin)
admin.site.register(models.TaskCenter,TaskCenterAadmin)
admin.site.register(models.TaskLog,TaskLogAdmin)



