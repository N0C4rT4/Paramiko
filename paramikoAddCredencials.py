import paramiko
from paramiko_expect import SSHClientInteraction
import getpass

####### Programa que se conecta por SSH a un dispositivo Cisco, introduciendo los datos necesarios para realizar la conexión
####### Datos necesario IP, Nombre usuario y password
##### getpass --> Secure password prompt

###PARA PODER EJECUTAR EL PROGRAMA SIN PROBLEMAS CON EL GETPASS EN EL PYCHARM, DEBEMOS IRNOS A :
########              RUN--> EDIT CONFIGURATIONS --> CLICAMOS EN EXECUTE --> EMULATE TERMINAL IN OUTPUT CONSOLE

#coleccion de datos necesarios el password lo usamos para no mostrar la contraseña en texto plano
ip = input("Entra la direccion ip: ")
username = input("Entra el nombre: ")
print("pide el pass")
password = getpass.getpass(prompt='entra el password: ')
print("todas las credenciales metidas")


#Inicializa la conexión Paramiko
remote_conn_client = paramiko.SSHClient()
remote_conn_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_client.connect(ip, username=username, password=password, allow_agent=False, look_for_keys=False)
print ("Conexión establecida con SSH %s" % ip)

#invokamo la consola
remote_conn = remote_conn_client.invoke_shell()
output = remote_conn.recv(1000).decode("utf-8")#almacena cadenas como unicode
prompt = output.strip()#strip copia los datos y los mete en el prompt
#remote_conn.close() socket

#conectamos con los datos para empezar a interactuar con la consola
remote_conn_client.connect(ip, username=username, password=password, allow_agent=False, look_for_keys=False)
interact = SSHClientInteraction(remote_conn_client, timeout=20, display=False)

#una vez logeados nos muestra por pantalla
#usamos expect para automatizar y poder interactuar
interact.expect(prompt)
interact.send('terminal length 0')
interact.expect(prompt)
cmd_output = interact.current_output_clean
interact.send('show running-config')
interact.expect(prompt)
cmd_output = interact.current_output_clean
print (cmd_output)

remote_conn_client.close()