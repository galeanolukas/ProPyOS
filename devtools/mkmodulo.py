#!/usr/bin/python3
import os
import subprocess as commands
montar = "mount -nt squashfs -o loop %s /tmp/%s"
desmon = "umount -nt squashfs /tmp/%s"

def Mk(ruta="", nombre="000"):
    ls = os.listdir(ruta)
    archivo = open("lista_" + nombre, "w")
    try:
        commands.getoutput("mkdir /tmp/" + nombre)
    except OSError:
        pass
    for mod in range(len(ls)):
        try:
            if nombre in ls[mod]:
                print ls[mod]
                pro = ruta + ls[mod]
                commands.getoutput(montar % (pro, nombre))
                commands.getoutput("cp -r /tmp/%s/* %s" % (nombre, nombre))
                commands.getoutput(desmon % nombre)
                archivo.write(ls[mod] + "\n")
            else:
                pass
        except OSError:
            print ("Modulo corrupto!!..")
            pass
    commands.getoutput("./dir2pro %s %s" % (nombre, nombre + ".pro"))
    print ("Se Creo el modulo %s..." % nombre)
    print ("Se creo lista %s de los modulos" % nombre)
    commands.getoutput("rm -R /tmp/" + nombre)
    archivo.close()
