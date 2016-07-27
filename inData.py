#!/bin/env python
#encoding:utf-8

import sys,time,os
import MySQLdb as mysql
conn=mysql.connect(user='root',passwd='zdsoft',db='falcon',host='192.168.16.63')
conn.autocommit(True)
cur=conn.cursor()

# 插入数据
def insert_data():
	home='/usr/local/src/python/project/mysite/monitor/'
	li={'nt':1,'js':2,'zj':3,'sd':4,'cs':5,'dg':6,'hbmy':7}
	for k,v in li.items():
		res=os.listdir(home+k)
		if len(res)==0:
			continue
		for name in res:
			with open(home + k + '/' + name) as f:
				data=eval(f.read())
				temp='"%s","%s","%s","%s","%s","%s","%s","%s","%s"'
				val='v,data["Host"],data["HostIp"],data["MemFree"],data["MemUsage"],data["MemTotal"],data["LoadAvg"],data["Time"],data["DiskUsage"]'
				sql='insert into stat values("%s","%s","%s","%s","%s","%s","%s","%s","%s")'%(v,data["Host"],data["HostIp"],data["MemFree"],data["MemUsage"],data["MemTotal"],data["LoadAvg"],data["Time"],data["DiskUsage"])
				try:
					cur.execute(sql)
				except Exception as e:
					print e

# 生成html网页
def save_html():
	html_save='<html>'
	html_save+='<head><title>Monitor_netstudy</title></head>'
	html_save+='<script>setTimeout("location.href=location.href",30000)</script>'
	html_save+='<body>'
	html_save+='<table border="1" align="center">'
	html_save+='<tr><td>主机名</td><td>主机ip</td><td>空闲内存</td><td>已使用内存</td><td>总内存</td><td>系统负载</td><td>主机时间</td><td>磁盘已使用</td></tr>'
	sql="SELECT DISTINCT a.host_name,a.hostip,a.mem_free,a.mem_usage,a.mem_total,a.load_avg,a.host_time,a.diskusage FROM stat a, (SELECT host_name ,hostip ,MAX(host_time) max_time FROM stat GROUP BY host_name,hostip) b WHERE a.host_name=b.host_name AND a.hostip=b.hostip AND a.host_time=b.max_time"
	cur.execute(sql)
	for c in cur.fetchall():
		html_save+='<tr><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td><td align="center">%s</td><td align="left">%s</td></tr>' %c
	html_save+='</table>'
	html_save+='</body>'
	html_save+='</html>'
	
	with open('/usr/local/src/python/project/mysite/monitor/scripts/web/templates/monitor.html','w') as f:
		f.write(html_save)
def start_html():
	insert_data()
	save_html()

start_html()


