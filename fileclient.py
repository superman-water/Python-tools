#_*_coding:utf-8_*_
# !/etc/bin/env python2.7
#coded by wangjd@2017
#file clients
import socket
import time
import struct
import os
#导入外部插件
#定义客户端，地址
sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#实例化socket
address=('127.0.0.1',9999)
#定义address
sc.connect(address)
#发起连接
while True:
    file_path="/home/wangjd/Desktop/test.txt"
    #定义要传输的文件地址
    file_info_size=struct.calcsize('128sl')
    #定义打包规则
    fhead=struct.pack('128sl',os.path.basename(file_path),os.stat(file_path).st_size)
    #定义头信息
    sc.send(fhead)
    #首先发送头部信息
    print("send file:",file_path)
    #打印文件信息
    if True:
        #一切正常，开始处理文件
        fo=open(file_path, 'rb')
        fileData=fo.read(1024)
        #读取文件数据，1024切分
        if not fileData:
            break
            #文件为空break
        else:
             sc.send(fileData)
            #发送数据，1024切分的数据
        fo.close()
        #发送结束，关闭文件。
        print("finish send..")
    sc.close()
    exit()


