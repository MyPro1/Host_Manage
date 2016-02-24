#coding:utf-8

import urllib,urllib2,json,time,datetime
import ConfigParser,commands
import threading
def request_get(host,port,url):
    """
    获取服务器端的数据包括主机信息和配置信息
    """
    req_url = "http://%s:%s%s" %(host,port,url)

    req = urllib2.urlopen(req_url)
    result = req.read()
    return result
    #print type(result)
    
def request_post(host,port,url,data):
    """
    向服务器端提交客户端执行后的数据
    """
    #url = "http://192.168.10.108:8000/api/task_result/1/"
    url_str = "http://%s:%s%s" %(host,port,url)
    data = urllib.urlencode(data)
    req = urllib2.urlopen(url_str, data)
    result = req.read()
    return result  

class server_conn(object):
    def __init__(self,conf):
        self.conf = conf

    def ParserConfiguration(self):
        """
        解析配置文件内容
        """
        #conf = 'watchdog.conf'
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.conf)
        # conf_list is a list
        self.conf_list = self.cf.items('watchdog client')
        # list transfered dict
        self.conf_dict = dict(self.conf_list)
        return self.conf_dict
        # {'post_url': '/api/Host/1/?format=json', 
        # 'get_url': '/api/Host/1/?format=json', 'server_port': '8000', 
        # 'server_ip': '192.168.10.108'}
        #self.server_ip = cf.get('watchdog client','server_ip')
        #self.server_port = cf.get('watchdog client','server_port')
        #self.server_get_url = cf.get('watchdog client','get_url')
        #self.server_post_url = cf.get('watchdog client','post_url')
        
    def pull_host_conf(self):
        """
        获取服务器端主机配置信息
        """
        conf_dict = self.ParserConfiguration()
        host = conf_dict['server_ip']
        port = conf_dict['server_port']
        url = conf_dict['get_url']
        host_conf = request_get(host,port,url)
        host_conf = json.loads(host_conf)
        return host_conf
    """  
    def update_host_conf(self):

        更新服务器端主机配置信息,首次运行获取服务器端配置信息,之后等待pull_interval获取服务器端配置信息
       
        pull_interval = 0
        run_time = 0
        while True:
            
            if time.time() - run_time >= pull_interval:
                self.pull_host_conf()
                host_conf = self.pull_host_conf()
                print host_conf
                pull_interval = host_conf['pull_interval']
                run_time = time.time()
                             
            next_run_time = pull_interval - (time.time() - run_time)
            print 'Program nex_run_time: %s' %next_run_time
            time.sleep(1)
"""
    def pull_task_conf(self):
        #这个函数已经废弃了
        conf_dict = self.ParserConfiguration()
        host = conf_dict['server_ip']
        port = conf_dict['server_port']
        url = conf_dict['get_task_url']
        task_conf = request_get(host,port,url)
        task_conf = json.loads(task_conf)
        if task_conf:
            # 获取最新任务
            self.last_task_conf = task_conf[-1]
            #print "\033[31;1mlast_task_conf:%s\033[0m" %last_task_conf
            self.task_id = self.last_task_conf['id']
        
            return self.last_task_conf
        else:
            self.last_task_conf = task_conf
            return self.last_task_conf
    
    # 运行这个函数可以使用多线程
    def run(self,last_task_conf):
        self.last_task_conf = last_task_conf
        if self.last_task_conf:
            # 等价于 self.last_task_conf['task_type']
            func = getattr(self, self.last_task_conf['task_type'])
            #print func
            command = self.last_task_conf['content']
            func(command)
        

        # 清空任务列表
        #self.task_conf = {}
        """
        func = getattr(self, task['task_type']) 
        # func = cmd
        result = func(task)
        # result = cmd(task)
        """
    def cmd(self,command):
        
        self.res = commands.getstatusoutput(command)
        print self.res
        self.post_data(self.res)
        return self.res
    
    data = {}
    def post_data(self,result):
        self.result = result
        host_conf = self.pull_host_conf()
        host_conf = json.dumps(host_conf)
        self.last_task_conf = json.dumps(self.last_task_conf)
        self.data = {
                     'self.result_type':self.result[0],
                     'self.result_data' :self.result[1],
                     'task_center':self.last_task_conf, 
                     'host_profile':host_conf,                 
                     }
        conf_dict = self.ParserConfiguration()
        host = conf_dict['server_ip']
        port = conf_dict['server_port']
        url = "/api/task_result/1/"
        result = request_post(host,port,url,self.data)
        return result
    def parse_task_conf(self):
        host_conf = self.pull_host_conf()
        host_conf_id = host_conf['id']
        host_conf_group = host_conf['group']
        self.last_task_conf_host = self.last_task_conf['host']
        self.last_task_conf_group = self.last_task_conf['group']
        if host_conf_id in self.last_task_conf_host:
            task_flage = True
        elif set(host_conf_group) & set(self.last_task_conf_group):
            task_flage = True
        else:
            task_flage = False
        if task_flage == True:
            t1 = threading.Thread(target=self.run,args=(self.last_task_conf,)) 
            t1.start()
            
    def main(self):
        
        pull_interval = 0
        run_time = 0
        conf_dict = self.ParserConfiguration()
        url = conf_dict['get_task_url']
        host = conf_dict['server_ip']
        port = conf_dict['server_port']

        while True:
            # 更新主机配置信息
            if time.time() - run_time >= pull_interval:
                #self.pull_host_conf()
                host_conf = self.pull_host_conf()
                print host_conf
                pull_interval = host_conf['pull_interval']
                #print "\033[1;31;40m =============================>pull_interval:\033[0m" ,pull_interval
                run_time = time.time()
                #print "\033[1;31;40m =============================>run_time:\033[0m" ,run_time            

            task_conf = request_get(host,port,url)
            print "\033[31;1mtask_conf::%s\033[0m" %task_conf
            task_conf = json.loads(task_conf)
            #第一次获取最后一次的任务，然后把api的地址，换成任务id号，因为任务的id号总比api地址大1
            #所以获取完成最后一次任务以后，task_conf字典就变为空了。当没有新任务的时候也就空了
            # 如果有新任务，那么id正好可以和新任务的api对上
            # 总的来说api的起始是从0开始，而任务的id是从1开始的
            if task_conf:
                self.last_task_conf = task_conf[-1]
                url = '/api/taskconf/%s/?format=json' %(self.last_task_conf['id'])
                #func = getattr(self, self.last_task_conf['task_type'])
                #command = self.last_task_conf['content']
                #func(command)
                self.parse_task_conf()
                
                
            """
            if self.last_task_conf:
                self.cf.read(self.conf)
                print "\033[32;1mself.cf.get('watchdog client', 'get_task_url')::%s\033[0m" %(self.cf.get('watchdog client', 'get_task_url'))
                self.cf.set( 'watchdog client', 'get_task_url', '/api/taskconf/%d/?format=json' %(self.task_id+1))
                print "\033[31;1mself.cf.get('watchdog client', 'get_task_url')::%s\033[0m" %(self.cf.get('watchdog client', 'get_task_url'))
                print "\033[31;1mlast_task_conf::%s\033[0m" %(self.last_task_conf)
                """
            next_run_time = pull_interval - (time.time() - run_time)
            print 'Program nex_run_time: %s' %next_run_time
            time.sleep(1)
    


if __name__ == '__main__':
    server = server_conn('watchdog.conf')
    server.main()
    