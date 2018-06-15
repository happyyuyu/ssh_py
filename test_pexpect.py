from pexpect import pxssh,spawn,EOF,TIMEOUT
from dotenv import find_dotenv,load_dotenv
import os
import test_scp

# username = input("Enter username: ")
# os.system("stty -echo")
# password = input('Enter Password: ')
# os.system("stty echo")
# print("\n")

hostname="localhost"
load_dotenv(find_dotenv())

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")

command="ls"

try:
    s = pxssh.pxssh()
    s.login(hostname, USERNAME, PASSWORD)
    s.sendline(command)
    s.prompt()             
    print(s.before.decode("UTF-8")) 
    test_scp.secure_copy(hostname, USERNAME, PASSWORD, "test.py", destination="~/Desktop")
    s.sendline("cd ~/Desktop")
    s.prompt()
    print(s.before.decode("UTF-8")) 
    s.sendline("python3 test.py")
    s.prompt()
    print(s.before.decode("UTF-8")) 
    s.sendline("pwd")
    s.prompt()
    print(s.before.decode("UTF-8")) 

except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)