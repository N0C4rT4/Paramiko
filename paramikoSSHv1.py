import paramiko
import time



#datos del router
ip_address="10.10.10.10"
username="cisco123"
password="cisco123"

#para establecer la conexión
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)


print ("Conexión establecida con: ", ip_address)

#llamamos a consola y realizamos las peticiones con los comandos
remote_connection = ssh_client.invoke_shell()
remote_connection.send(b'enable \n')
remote_connection.send(b'configure terminal \n')
remote_connection.send(b'int loop 0 \n')
remote_connection.send(b'ip address 1.1.1.1 255.255.255.255 \n')
remote_connection.send(b'do show run  \n')
time.sleep(3)

#metemos la info recogida recv para leer y printarlo, sockets
output = remote_connection.recv(65535)
print (output.decode('ascii'))

ssh_client.close()
