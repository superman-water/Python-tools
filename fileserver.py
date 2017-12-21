#_*_coding:utf-8_*_
# !/etc/bin/env python2.7
#coded by wangjd@2017
#socket file server
import socket
import SocketServer
import time
import struct
import os
#导入外部插件
#定义服务器，地址，端口
address=("",9999)
#(ip,port)
class MyRequestHandler(SocketServer.BaseRequestHandler):
    #继承SocketServer请求处理的类
    def handle(self):
        #重写handle方法
        print("connect from :",self.client_address)
        # 打印客户端连接的IP
        while True:
            #没有报错执行
            fileinfo_size=struct.calcsize('128sl')
            #定义文件信息，文件名为128bytes长度
            self.buf=self.request.recv(fileinfo_size)
            #接受的是客户端发送过来的头部信息
            if self.buf:
                self.filename,self.filesize=struct.unpack('128sl',self.buf)
                #解包得到文件名和文件大小
                print("filename and size:",self.filename,self.filesize)
                self.filename=os.path.join('/home/wangjd/Desktop/','new'+self.filename.strip('\00'))
                #重新处理文件名，使用trip删除打包时候的多余空字符
                recvd_size=0
                #初始化接受了的文件大小
                file=open(self.filename,'wb')
                #打开文件
                print("start recv data..")
                while not recvd_size==self.filesize:
                    #当没接收完时候执行
                    if self.filesize -recvd_size > 1024:
                        rdata=self.request.recv(1024)
                        recvd_size+=len(rdata)
                        #叠加大小
                    else:
                        rdata=self.request.recv(self.filesize-recvd_size)
                        recvd_size=self.filesize
                    file.write(rdata)
                    #写入
                file.close()
                #关闭文件
                SocketServer
                print('data.....finish')
if __name__ == '__main__':
        tcpSever=SocketServer.ThreadingTCPServer(address,MyRequestHandler)
        print('waiting...')
        tcpSever.serve_forever()
        #保持