import tkinter as t
from tkinter import messagebox
from matplotlib.pyplot import*
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
from math import*
ven=t.Tk()
ven.title("GRAFICADORA DE FUNCIONES")
ven.geometry("900x800")
style.use('fivethirtyeight')
figura=Figure()
ax=figura.add_subplot(111)
cvs=FigureCanvasTkAgg(figura,ven)
cvs.draw()
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)
tlb=NavigationToolbar2Tk(cvs,ven)
tlb.update()
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)

rango1=False
rango2=""
rango3=""

fun={"cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","ln":"np.log","pi":"np.pi","sin":"np.sin","floor":"np.floor","arccos":"np.arccos","arcsin":"np.arcsin","arctan":"np.arctan","logb10":"np.log10","cosh":"np.cosh","sinh":"np.sinh","tanh":"np.tanh"}

def reemplaza(p):
    for i in fun:
        if i in p:
            p=p.replace(i,fun[i])
    return p
       
def animate(i):
    global rango1
    global rango2
    if rango1==True:
        try:
            min=float(rango3[0]);max=float(rango3[1])
            if min<max:
                x=np.arange(min,max,0.01)
                rango2=[min,max]
            else:
                rango1=False
        except:
            messagebox.showwarning("El rango resulta incorrecto")
            rango1=False
            entra_var.delete(0,len(entra_var.get()))
    else:
        if rango2!="":
            x=np.arange(rango2[0],rango2[1],0.01)
        else:
            x=np.arange(0,10,0.01)
    try:
        sl=eval(graf_dt)
        ax.clear()
        ax.plot(x,sl)
    except:
        ax.plot()
    ax.axhline(0,color="black")
    ax.axvline(0,color="gray")
    ani.event_source.stop()
def represent():
    global graf_dt
    global rango3
    global rango1
    tx_original=entra_func.get()
    if entra_var.get() !="":
        rann=entra_var.get()
        rango3=rann.split(",")
        rango1=True
    graf_dt=reemplaza(tx_original)
    ani.event_source.start()
ani=anim.FuncAnimation(figura,animate,interval=1000)
show()




bo1=t.Button(ven,text="graficar", command=represent)
entra_func=t.Entry(ven,width=60)
entra_var=t.Entry(ven,width=20)
bo1.pack(side=t.BOTTOM)
entra_var.pack(side=t.RIGHT)
entra_func.pack(side=t.BOTTOM)

ven.mainloop()