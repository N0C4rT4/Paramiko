from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import time
import datetime


#cadenas de tiempo para poder guardar el archivo con la fecha exacta y la hora
TiempoActual= datetime.datetime.now().replace(microsecond=0)

#lista de las ip de los routers
ip_lista = open('ListaIPS')

#recorrido para que pueda lea todas las ip del archivo, damos por hecho q el username, pass son iguales para todos
for ip in ip_lista:
    print ('\n  '+ ip.strip() + ' \n')
    router = {
    'ip':   ip,
    'username': 'cisco123',
    'password': 'cisco123',
    'device_type': 'cisco_ios',
    }
##creamos una excepciones, conectado, no conectado, creacion de la bbdd en txt
    try:
        net_connect = ConnectHandler(**router)#llamamos a los datos
    except NetMikoTimeoutException:
        print ('Dispositivo no accesible.')
        continue
    except AuthenticationException:
        print ('Fallo de autenticación.')
        continue
    except SSHException:
        print ('Creación de conexión por SSh en el dispositivo.')
        continue

    print ('Iniciando el salvado de datos en la BBDD')
    salida = net_connect.send_command('show run')
##creamos el fichero con el nombre de la ip del router
    fsaved = open("router_" + ip, 'w')
    fsaved.write(salida)
    fsaved.close
    print ('Finalizada la BBDD')
