import sys, paramiko
from dotenv import find_dotenv,load_dotenv
import os

load_dotenv(find_dotenv())

USERNAME = os.getenv("username")
PASSWORD = os.getenv("password")
# username = input("Enter username: ")
# os.system("stty -echo")
# password = input('Enter Password: ')
# os.system("stty echo")

hostname="localhost"

command="ls"

#print(USERNAME)
try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(hostname, username=USERNAME, password=PASSWORD)
    stdin,stdout,stderr = client.exec_command(command)
    # session = client.get_transport().open_session()
    # paramiko.agent.AgentRequestHandler(session)
    # stdin,stdout,stderr = session.exec_command(command)
    out = stdout.read()
    print(out.decode('UTF-8'))
    # session.close()

finally:
    client.close()