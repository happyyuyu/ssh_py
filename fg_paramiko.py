import sys, paramiko, re
from dotenv import find_dotenv,load_dotenv
import os
import time

load_dotenv(find_dotenv())
# HOSTNAME = os.getenv("hostname")
# USERNAME = os.getenv("username")
# PASSWORD = os.getenv("password")

HOSTNAME = os.getenv("fort_hostname")
USERNAME = os.getenv("fort_username")
PASSWORD = os.getenv("fort_password")

def send_cmd(chan, cmd):
    chan.send(cmd+'\n')
    while not chan.recv_ready(): 
        time.sleep(1)
    out = chan.recv(1024)
    return out.decode("UTF-8")

def show_all(chan):
    res = send_cmd(chan, "show")
    temp_res = send_cmd(chan, "n")
    res += temp_res
    # print(res)
    while re.search("--More--", temp_res):
        # temp_res=send_cmd(chan, "n")
        temp_res = send_cmd(chan, "n")+send_cmd(chan, "n")
        res+=temp_res
        # print(temp_res)
    return res

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(HOSTNAME, username=USERNAME, password=PASSWORD)
    channel = client.invoke_shell() 
    # print(send_cmd(channel, "ls"))
    # print(send_cmd(channel, "cd Desktop"))
    # print(send_cmd(channel, "pwd"))
    print(send_cmd(channel, "config vdom"))
    print(send_cmd(channel, "edit root"))
    print(send_cmd(channel, "config user local"))
    print(show_all(channel))


finally:
    client.close()