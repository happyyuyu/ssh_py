import pexpect
import os
# import scp
from paramiko import WarningPolicy,SSHClient
from scp import SCPClient
from dotenv import find_dotenv,load_dotenv

def secure_copy(hostname, username, password, filename, destination="~/"):

    # try:
    #     #make sure in the above command that username and hostname are according to your server
    #     scp_command = 'sudo scp ./test.py '+ username+ "@" + hostname + ':~/Desktop/'
    #     # print(scp_command)
    #     child = pexpect.spawn(scp_command)
    #     child.expect(["assword:"])      
    #     child.sendline(password)
    #     child.expect(pexpect.EOF, timeout=2)

    # except Exception as e:
    #     print("Oops Something went wrong buddy")
    #     print(e)
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(WarningPolicy)
    ssh.connect(hostname, username=username, password=password)
    with SCPClient(ssh.get_transport()) as scp:
        scp.put(filename, destination) # Copy to the server


def main():
    # username = input("Enter username: ")
    # os.system("stty -echo")
    # password = input('Enter Password: ')
    # os.system("stty echo")
    # print("\n")

    load_dotenv(find_dotenv())

    USERNAME = os.getenv("username")
    PASSWORD = os.getenv("password")
    hostname="localhost"
    filename='test.py'
    destination='~/Desktop/test.py'
    secure_copy(hostname, USERNAME, PASSWORD, filename, destination=destination)

if __name__ == "__main__":
    main()