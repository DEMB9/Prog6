from cProfile import label
from cgitb import text
import random
from sqlite3 import Row
from tkinter import *
import time

kilometros = [1,3,6,9,12,15,18,21]

condi = 1

info = {1:["John","Smith","ABC123",10,25,0],
2:["Juan","Quevedo","QWE125",50,25,1],
3:["Carlos","Tangana","QFE125",57,15,0],
4:["Sofia","Garcia","UIO243",26,20,1],
5:["Omar","Montes","PAS693",24,25,0],
6:["Karen","Pikety","DFG193",27,5,1],
7:["Daniel","Sarmiento","HJK103",100,35,0],
8:["Pedro","Alvarado","KLZ423",150,25,1],
9:["Sergio","Almeida","XCV129",24,100,0],
10:["Maria","Platini","BNM523",8,25,1],
11:["Harry","Tolkien","LRD183",200,25,0]}


raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#primera consulta
name=Entry(miFrame)
name.grid(row=1,column=1)

nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=1,column=0)
#fin primera consulta

#Segunda consulta
telefono=Entry(miFrame)
telefono.grid(row=2,column=1)

telefonoLabel = Label(miFrame, text="Numero de contacto")
telefonoLabel.grid(row=2,column=0)
#Fin segunda consulta


#Tercera consulta
dist = Entry(miFrame)
dist.grid(row=3,column=1)

distLabel = Label(miFrame, text="Distancia (km)")
distLabel.grid(row=3,column=0)
#fin Tercera consulta

#Cuarta consulta
salidacalle=Entry(miFrame)
salidacalle.grid(row=4,column=1)

salidacalleLabel= Label(miFrame, text="Calle de salida")
salidacalleLabel.grid(row=4,column=0)
#fin cuarta consulta

#Quinta consulta
salidacarrera=Entry(miFrame)
salidacarrera.grid(row=5,column=1)

salidacarreraLabel= Label(miFrame, text="Carrera de salida")
salidacarreraLabel.grid(row=5,column=0)
#fin quinta consulta

#sexta consulta
llegadacalle=Entry(miFrame)
llegadacalle.grid(row=6,column=1)

llegadacalleLabel= Label(miFrame, text="Calle de llegada")
llegadacalleLabel.grid(row=6,column=0)
#fin quinta consulta

#septima consulta
llegadacarrera=Entry(miFrame)
llegadacarrera.grid(row=7,column=1)

llegadacarreraLabel= Label(miFrame, text="Carrera de llegada")
llegadacarreraLabel.grid(row=7,column=0)
#fin septima consulta
espacio= Label(miFrame, text="")
espacio.grid(row=8,column=0)
#boton de evalución
my_string_var = StringVar()
count=0
def codigoBoton():
    #Saludo
    ename=name.get()

    prname = Label(miFrame,text="Estimado "+ename)
    prname.grid(row=9,column=0)
    #Fin saludo

    #Calculo de diferencias de distancia y radio

    distancia = int(dist.get())
    r = distancia*10
    c = (int(salidacalle.get())-int(llegadacalle.get()))**2+(int(salidacarrera.get())-int(llegadacarrera.get()))**2

    if c < r**2:
        rew = Label(miFrame,text="Se encuentra dentro del rango")
        rew.grid(row=10,column=0)

        trayecto = (((int(salidacalle.get())-int(llegadacalle.get()))**2+(int(salidacarrera.get())-int(llegadacarrera.get()))**2)**(1/2))/10

        tre = Label(miFrame,text=str(round(trayecto,3))+" Km")
        tre.grid(row=11,column=0)

        #Inicio calculo del feed(costo del envio)
        if trayecto < 2:
            feed = 2000
        elif trayecto >=2 and trayecto < 5:
            feed = 5000
        elif trayecto >=5 and trayecto <10:
            feed = 10000
        elif trayecto >= 10:
            feed = 20000
        
        costo = Label(miFrame, text="El costo del envío será de: "+ str(feed)+" + gasto de transporte")
        costo.grid(row=12,column=0)
        
        q=0
        count = 0

        for i in info:
            if info[i][5] == 1:
                colab = Label(miFrame, text="En breve "+ info[i][0] +" "+ info[i][1])
                espacio2 = Label(miFrame, text="")
                espacio2.grid(row=14,column=0)
                q=1
                count = i
                break;

        if q == 0:
            colab = Label(miFrame, text="En estos momentos no hay personal disponible. Intente mas tarde")
            colab.grid(row=13,column=0)
        
        



    else:
        rew = Label(miFrame,text="Se encuentra fuera del rango")
        rew.grid(row=10,column=0)

        trayecto = (((int(salidacalle.get())-int(llegadacalle.get()))**2+(int(salidacarrera.get())-int(llegadacarrera.get()))**2)**(1/2))/10

        tre = Label(miFrame,text=str(round(trayecto,3))+" Km")
        tre.grid(row=11,column=0)

        condi = 0


#Generar Tikcet



def generador():
    ventana = Toplevel(raiz)

    ventana.geometry("330x200")

    Label(ventana, text="Ticket de envío").pack(anchor=CENTER)

    for i in info:
        if info[i][5] ==1:
            Label(ventana,text="Colaborador: "+info[i][0]+" "+info[i][1]).pack(anchor=CENTER)
            info[i][5] = 0
            Label(ventana, text="Placa: "+info[i][2]).pack(anchor=CENTER)
            Label(ventana, text="Comisión por combustible: "+str(info[i][4]/100)).pack(anchor=CENTER)
            Label(ventana, text="Nuestro colaborador se comunicará a: "+ telefono.get()).pack(anchor=CENTER)
            Label(ventana, text="Recoge en calle "+salidacalle.get()+" con carrera "+salidacarrera.get()).pack(anchor=CENTER)
            Label(ventana, text="Entrega en calle "+llegadacalle.get()+" con carrera "+llegadacarrera.get()).pack(anchor=CENTER)
            codigo = random.randint(1000,9999)
            Label(ventana,text="Codigo de Ticket: "+ str(codigo)).pack(anchor=CENTER)
            
            trayecto = (((int(salidacalle.get())-int(llegadacalle.get()))**2+(int(salidacarrera.get())-int(llegadacarrera.get()))**2)**(1/2))/10
            if trayecto < 2:
                feed = 2000
            elif trayecto >=2 and trayecto < 5:
                feed = 5000
            elif trayecto >=5 and trayecto <10:
                feed = 10000
            elif trayecto >= 10:
                feed = 20000

            Label(ventana,text= "El total a pagar es: "+ str((feed+((info[i][4]/100)*feed)))).pack(anchor=CENTER)





            break;




boton=Button(raiz,text="Consultar", command=codigoBoton)
boton.pack()

generar = Button(raiz,text="Generar pedido", command=generador)
generar.pack()



raiz.mainloop()