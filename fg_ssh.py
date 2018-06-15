import sys, paramiko
from pexpect import pxssh,spawn,EOF,TIMEOUT
from dotenv import find_dotenv,load_dotenv
import os

def send_n_print(client, command):
    stdin,stdout,stderr = client.exec_command(command)
    # out = stdout.read()
    # print(out.decode('UTF-8'))
    type(stdin)
    return stdout

load_dotenv(find_dotenv())
HOSTNAME = os.getenv("fort_hostname")
USERNAME = os.getenv("fort_username")
PASSWORD = os.getenv("fort_password")

print(HOSTNAME, USERNAME)
print(PASSWORD)
# try:
#     s = pxssh.pxssh()
#     s.login(HOSTNAME, USERNAME, PASSWORD, auto_prompt_reset=False, port=22)
#     s.sendline("config vdom")
#     s.sendline("edit root")
#     s.sendline("config user local")
#     s.prompt()
#     print(s.before.decode("UTF-8")) 
#     s.sendline("show")
#     s.prompt()
#     print(s.before.decode("UTF-8")) 
#     more = s.expect(["--More--", TIMEOUT, EOF], timeout=2)
#     while(more==0):
#         # print("more")
#         s.prompt()
#         print(s.before.decode("UTF-8")) 
#         s.sendline("n")
#         more = s.expect(["--More--","Unknown action 0", TIMEOUT, EOF], timeout=2)
#         if more == 1 or more == 2 or more == 3:
#             break
#     s.prompt()
#     print(s.before.decode("UTF-8")) 
    
# except pxssh.ExceptionPxssh as e:
#     print("pxssh failed on login.")
#     print(e)

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(HOSTNAME, username=USERNAME, password=PASSWORD)
    stdout = send_n_print(client, "config vdom /r edit root/r config user local/n/r show | newuser/n")
    stdout.channel.recv_exit_status()
    # stdout = send_n_print(client, "edit root")
    out = stdout.readlines()
    for line in out:
        print(line)
    # stdout = send_n_print(client, "edit root")

    # send_n_print(client, "config user local")
    # send_n_print(client, "show | newuser")
    out = stdout.read()
    print(out.decode('UTF-8'))


finally:
    client.close()