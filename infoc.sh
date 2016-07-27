#!/usr/bin/bash

HOME_DIR="/usr/local/src/python/project/mysite/monitor/scripts"
TIME=$(date "+ %Y-%m-%d-%H:%M:%S")

#本地测试
#echo "从本地192.168.22.221获取信息文件 $TIME" >> $HOME_DIR/info.log
#scp 192.168.22.221:/usr/local/src/work/local/* /usr/local/src/python/project/mysite/monitor/local/

#南通平台
echo "从南通平台101.71.43.98获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@101.71.43.98:/usr/local/src/work/nt/* /usr/local/src/python/project/mysite/monitor/nt/

echo "从东莞平台113.108.127.105获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@113.108.127.105:/usr/local/src/work/dg/* /usr/local/src/python/project/mysite/monitor/dg/

echo "从常熟平台218.4.174.9获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@218.4.174.9:/usr/local/src/work/cs/* /usr/local/src/python/project/mysite/monitor/cs/

echo "从山东平台119.188.75.114获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@119.188.75.114:/usr/local/src/work/sd/* /usr/local/src/python/project/mysite/monitor/sd/

echo "从湖北迈异平台116.211.105.24获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@116.211.105.24:/usr/local/src/work/hbmy/* /usr/local/src/python/project/mysite/monitor/hbmy/

echo "从江苏平台58.215.144.49获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@58.215.144.49:/usr/local/src/work/js/* /usr/local/src/python/project/mysite/monitor/js/

echo "从浙江平台101.69.170.66获取信息文件 $TIME" >>$HOME_DIR/info.log
scp -P 65422 winupon@101.69.170.66:/usr/local/src/work/zj/* /usr/local/src/python/project/mysite/monitor/zj/




# 各服务器信息插入数据库，生成html网页文件
python /usr/local/src/python/project/mysite/monitor/scripts/inData.py &
