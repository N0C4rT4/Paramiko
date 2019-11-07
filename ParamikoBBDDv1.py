import paramiko
import time
from getpass import getpass
import datetime

#formato fecha, hora, minutos, segundos
# tiempoactual=datetime.datetime.now().replace(microsecond=0)



listaDispositivos = open('ListaIPS')
for router in listaDispositivos:
    router=router.strip()
    print('\n Conectado con los dispositivos' + router + '\n' )
    session= paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect(router, port=22,
                    username='cisco123', password='cisco123', allow_agent=False, look_for_keys=False)
    acceso_dispos= session.invoke_shell()
    acceso_dispos.send (b'terminal len 0 \n')
    acceso_dispos.send(b'show run \n')

    time.sleep(5)
    salida= acceso_dispos.recv(65000)
    print(salida.decode('ascii'))


    # fichero=open('Dipositivo ' + router + str(tiempoactual), 'w')
    fichero=open('Dispositivo' + router, 'w')
    fichero.write(salida.decode('ascii'))
    fichero.close()

    session.close
