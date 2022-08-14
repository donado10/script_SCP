from click import option
from paramiko import SSHClient
from scp import SCPClient
import time

ssh = SSHClient()
ssh.load_system_host_keys()

#Information de la machine hôte Linux
hostname = ''
port = 22
username = 'username'
password = 'password'
ssh.connect(hostname= hostname,port = port, username = username, password = password,look_for_keys=False, allow_agent=False)


scp = SCPClient(ssh.get_transport())


path_linux = '/home/ado/'
path_windows = 'C:\\Users\\LBC\\Documents\\Projet_Mémoire\\'
folder = 'Monitoring_Project'

print("Connexion réussie...\n")

option = 0
while option != 3:
    print("----------------------------------------------------")
    print("1- SCP windows to UbuntuServer\n")
    print("2- SCP UbuntuServer to windows\n")
    print("3- Quiter\n")
    option = int(input("Veuillez entrer un choix svp : "))
    print("----------------------------------------------------")

    if option == 1:
        shell = ssh.invoke_shell()
        shell.send('rm -rf ' + path_linux + folder + "\n")
        time.sleep(1)
        scp.put(path_windows + folder, recursive=True, remote_path=path_linux)
        print("Upload over ...!!")
    elif option == 2:
        scp.get(remote_path= path_linux + folder,recursive=True,local_path=path_windows)
        print("Download over ...!!")
    elif option == 3:
        print("Closing...")
    else:
        print("Choix inexistant !!")
scp.close()