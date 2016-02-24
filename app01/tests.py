#coding:utf-8

files = '/etc/zabbix/zabbix_agentd.conf'
content = """
UserParameter=procexist[*],/home/zabbix/monitor/zabbix_procexist.sh $1
UserParameter=fileexist[*],/home/zabbix/monitor/fileexist.sh $1
UserParameter=filesize[*],/home/zabbix/monitor/filesize.sh $1
"""

f = open(files,'a')
f.write(content)
f.close()