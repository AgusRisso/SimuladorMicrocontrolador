
from os import environ
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from random import *
import commands
import os, sys
import subprocess
import threading
import time

app=Flask(__name__)
productor=threading.Thread()
iniciar=0
@app.route('/')

@app.route('/index')
def index():
    global iniciar
    if iniciar==1:
        iniciar=0
    return render_template(
        'index.html',
        title="Pagina Inicio",
        year=datetime.now().year
        )

@app.route('/simulador',  methods = ['GET','POST'])
def simulador():
    global iniciar
    lista=[0,0,0,0]
    if iniciar==0:
        iniciar=1
        productor = threading.Thread(target=producir, args=(2,))
        productor.setDaemon(True)
        productor.start() 
    consumir(lista)
    t=lista[0]
    h=lista[1]
    p=lista[2]
    v=lista[3]
    promedio=[0,0,0,0]
    prom(promedio,t,h,p,v)
    promediot=promedio[0]
    promedioh=promedio[1]
    promediop=promedio[2]
    promediov=promedio[3]
    if request.method == 'POST':
        data = request.form
        value = int(data["frec"])
        return render_template(
           'simulador.html',
            value=value,
            val=datetime.now().time(),
            t=t,
            h=h,
            p=p,
            v=v,
            promediot=promediot,
            promedioh=promedioh,
            promediop=promediop,
            promediov=promediov,
            )
    else:
        return render_template(
           'simulador.html',
            value=2000,
            val=datetime.now().time(),
            t=t,
            h=h,
            p=p,
            v=v,
            promediot=promediot,
            promedioh=promedioh,
            promediop=promediop,
            promediov=promediov,
        )

def consumir(lista):
    file = open("datos.txt", "r")
    linea=file.readline();
    t,h,p,v=linea.split(",")
    lista[0]=t
    lista[1]=h
    lista[2]=p
    lista[3]=v
    file.close()
    return

def producir(t_muestreo):
    global iniciar
    while iniciar==1:
        time.sleep(t_muestreo)
        file = open("datos.txt", "w") 
        t= randint(1,100)
        h=randint(1,100)
        p=randint(1,100)
        v=randint(1,100)
        file.write(str(t)+","+str(h)+","+str(p)+","+str(v))
        file.close()
    return

def prom(promedio,t,h,p,v):
    file = open("datos.txt", "r")
    linea=file.readline();
    t,h,p,v=linea.split(",")
    file.close()
    file = open("promediostemp.txt", "r")
    lineatemp=file.readline();
    uno,dos,tres,cua,cin,seis,siet,ocho,nuev,diez=lineatemp.split(",")
    diez=nuev
    nuev=ocho
    ocho=siet
    siet=seis
    seis=cin
    cin=cua
    cua=tres
    tres=dos
    dos=uno
    uno=t
    promedio[0]=(int(uno)+int(dos)+int(tres)+int(cua)+int(cin)+int(seis)+int(siet)+int(ocho)+int(nuev)+int(diez))/10
    file.close()
    file = open("promediostemp.txt", "w")
    file.write(str(uno)+","+str(dos)+","+str(tres)+","+str(cua)+","+str(cin)+","+str(seis)+","+str(siet)+","+str(ocho)+","+str(nuev)+","+str(diez))
    file.close()

    file = open("promedioshum.txt", "r")
    lineatemp=file.readline();
    uno,dos,tres,cua,cin,seis,siet,ocho,nuev,diez=lineatemp.split(",")
    diez=nuev
    nuev=ocho
    ocho=siet
    siet=seis
    seis=cin
    cin=cua
    cua=tres
    tres=dos
    dos=uno
    uno=h
    promedio[1]=(int(uno)+int(dos)+int(tres)+int(cua)+int(cin)+int(seis)+int(siet)+int(ocho)+int(nuev)+int(diez))/10
    file.close()
    file = open("promedioshum.txt", "w")
    file.write(str(uno)+","+str(dos)+","+str(tres)+","+str(cua)+","+str(cin)+","+str(seis)+","+str(siet)+","+str(ocho)+","+str(nuev)+","+str(diez))
    file.close()
    
    file = open("promediospre.txt", "r")
    lineatemp=file.readline();
    uno,dos,tres,cua,cin,seis,siet,ocho,nuev,diez=lineatemp.split(",")
    diez=nuev
    nuev=ocho
    ocho=siet
    siet=seis
    seis=cin
    cin=cua
    cua=tres
    tres=dos
    dos=uno
    uno=p
    promedio[2]=(int(uno)+int(dos)+int(tres)+int(cua)+int(cin)+int(seis)+int(siet)+int(ocho)+int(nuev)+int(diez))/10
    file.close()
    file = open("promediospre.txt", "w")
    file.write(str(uno)+","+str(dos)+","+str(tres)+","+str(cua)+","+str(cin)+","+str(seis)+","+str(siet)+","+str(ocho)+","+str(nuev)+","+str(diez))
    file.close()
    
    file = open("promediosvien.txt", "r")
    lineatemp=file.readline();
    uno,dos,tres,cua,cin,seis,siet,ocho,nuev,diez=lineatemp.split(",")
    diez=nuev
    nuev=ocho
    ocho=siet
    siet=seis
    seis=cin
    cin=cua
    cua=tres
    tres=dos
    dos=uno
    uno=v
    promedio[3]=(int(uno)+int(dos)+int(tres)+int(cua)+int(cin)+int(seis)+int(siet)+int(ocho)+int(nuev)+int(diez))/10
    file.close()
    file = open("promediosvien.txt", "w")
    file.write(str(uno)+","+str(dos)+","+str(tres)+","+str(cua)+","+str(cin)+","+str(seis)+","+str(siet)+","+str(ocho)+","+str(nuev)+","+str(diez))
    file.close()

    return

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 80
    app.run(HOST, PORT,debug=True)