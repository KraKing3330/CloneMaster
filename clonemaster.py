#! bin/python
import os

#Colores
reinicio = '\033[0m'
negrita = '\033[01m'
desactivar = '\033[02m'
subrayar = '\033[04m'
inversa = '\033[07m'
tachada = '\033[09m'
invisible = '\033[08m'

negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
naranja = '\033[33m'
azul = '\033[34m'
morado = '\033[35m'
cyan = '\033[36m'
gris_claro = '\033[37m'
gris_oscuro = '\033[90m'
rojo_claro = '\033[91m'
verde_claro = '\033[92m'
amarillo = '\033[93m'
azul_claro = '\033[94m'
rosado = '\033[95m'
cyan_claro = '\033[96m'

def scl ( ) :
    os.system ( " sleep 1 " )
    os.system ( " clear " )

#BANNER
def banner ( ) :
    print ( gris_oscuro , '''
Kr4K1ng
      ____ _                    __  __           _
     / ___| | ___  _ __   ___  |  \/  | __ _ ___| |_ ___ _ __
    | |   | |/ _ \| '_ \ / _ \ | |\/| |/ _` / __| __/ _ \ '__|
    | |___| | (_) | | | |  __/ | |  | | (_| \__ \ ||  __/ |
     \____|_|\___/|_| |_|\___| |_|  |_|\__,_|___/\__\___|_|

Pulse CTRL + C para salir
    ''' , reinicio )

scl ( )
banner ( )

print ( negrita , verde , '''
 __Archivos en Directorio
|
V''', reinicio , subrayar , reinicio )
os.system ( " ls " )
print ( " " )

name = input ( negrita + rojo_claro + "Archivo a clonar >>> " + cyan )

print ( " " )

os.system ( " mkdir .file " )

def clone ( ) :
    os.system( "cp -v --force --backup=numbered " + name + " {}".format (".file") )

while True:
    clone ( )
    

reinicio
#Fin
