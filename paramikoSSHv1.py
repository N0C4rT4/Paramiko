import paramiko
import time

ip_address="10.10.10.10"
username="cisco123"
password="cisco123"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)


print ("Successful connection", ip_address)


remote_connection = ssh_client.invoke_shell()

remote_connection.send("enable \n")
remote_connection.send("configure terminal \n")
remote_connection.send("int loop 0 ")
remote_connection.send("ip address 1.1.1.1 255.255.255.255 \n")

output = remote_connection.recv(65535)
salida=remote_connection.send("do show ip run \n")
print (output)
