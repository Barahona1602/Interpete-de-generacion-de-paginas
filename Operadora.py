from tkinter import *
import webbrowser
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import scrolledtext as st
import numpy as np
from tkinter import messagebox as MessageBox
import ntpath
import os,time
import pyautogui as pag
from analizador import Analizador


global nuevoarchivo1



def __init__():
    Analizador=Analizador()



#Method to open a file
def abrirArchivo():
        cuadro.delete("1.0","end")
        try:  
            global archivo1   
            archivo1 = filedialog.askopenfilename(title="Abrir archivo", initialdir="C:/", filetypes=(("txt files",".txt"),("Todos los archivos",".*")))
        except:
            print("No se agregaron archivos")
            global nombrearchivo
        nombrearchivo=ntpath.basename(archivo1)
        nombrearchivo=nombrearchivo.replace(".txt","")
        nombrearchivo=nombrearchivo.replace(".html","")
        Datos = open(archivo1, "r", encoding='utf-8')
        for line in Datos:
            cuadro.insert(END,line)
        





#Method for new document 
def nuevo():
    nuevo = tk.Tk()
    nuevo.geometry("500x150")
    nuevo["bg"]='#222831'
    nuevo.title("Guardar como")
    fontStylelbl = tkFont.Font(family='Open Sans Light', size='14', weight='bold')
    lbl1=tk.Label(nuevo, text="Elija el nombre de su archivo", font=fontStylelbl, fg="#DDDDDD", bg="#222831").place(x=25, y=25)
    entry1=tk.Entry(nuevo, font=fontStylelbl, fg="#222831", bg="#DDDDDD", width="30")
    entry1.place(x=25, y=65)


    def botonguardar():
        global nombrearchivo
        nombrearchivo=entry1.get()
        nuevoarchivo1=open(nombrearchivo+".txt","w+",encoding='utf-8')
        nuevoarchivo1.writelines(cuadro.get("1.0","end-1c"))
        print(nombrearchivo)
        MessageBox.showinfo("Guardar como", "Archivo guardado correctamente")
        nuevo.destroy()
        cuadro.delete("1.0","end")
    bttn1 = tk.Button(nuevo, text="Guardar como", font=fontStylelbl, command=botonguardar, fg="#30475E", bg="#DDDDDD").place(x=325, y=60)
    









#---------------------------------------------------
#---------------------------------------------------





#Method to save file
def guardar():
    nuevoarchivo1=open(nombrearchivo+".txt","w+",encoding='utf-8')
    nuevoarchivo1.writelines(cuadro.get("1.0","end-1c"))





#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------





#Method to save as file 
def guardarcomo():
    
    guardarcomo = tk.Tk()
    guardarcomo.geometry("500x150")
    guardarcomo["bg"]='#222831'
    guardarcomo.title("Guardar como")
    fontStylelbl = tkFont.Font(family='Open Sans Light', size='14', weight='bold')
    lbl1=tk.Label(guardarcomo, text="Elija el nombre de su archivo", font=fontStylelbl, fg="#DDDDDD", bg="#222831").place(x=25, y=25)
    entry1=tk.Entry(guardarcomo, font=fontStylelbl, fg="#222831", bg="#DDDDDD", width="30")
    entry1.place(x=25, y=65)


    def botonguardar():
        global nombrearchivo
        nombrearchivo=entry1.get()
        nuevoarchivo1=open(nombrearchivo+".txt","w+",encoding='utf-8')
        nuevoarchivo1.writelines(cuadro.get("1.0","end-1c"))
        print(nombrearchivo)
        MessageBox.showinfo("Guardar como", "Archivo guardado correctamente")
        guardarcomo.destroy()
    bttn1 = tk.Button(guardarcomo, text="Guardar como", font=fontStylelbl, command=botonguardar, fg="#30475E", bg="#DDDDDD").place(x=325, y=60)





#---------------------------------------------------
#---------------------------------------------------




#Method to analyze 
def analizar():
    Analizador(archivoimp=archivo1).compile()
    Analizador.htmlanalizar()




#---------------------------------------------------
#---------------------------------------------------




#Method to display errors
def errores():
   Analizador.htmlerrores() 




#---------------------------------------------------
#---------------------------------------------------


#Exit command
def salirPro():
    exit()





#---------------------------------------------------
#---------------------------------------------------


#Command to show user manual
def manualusuario():
    manualuser = 'ManualDeUsuarioLFP_202109715_Proyecto1.pdf'
    webbrowser.open_new(manualuser)





#---------------------------------------------------
#---------------------------------------------------



#Command to show technical manual
def manualtecnico():
    manualtecnico = 'ManualTécnicoLFP_202109715_Proyecto1.pdf'
    webbrowser.open_new(manualtecnico)





#---------------------------------------------------
#---------------------------------------------------



#Command to display info
def info():
    info = tk.Tk()
    info.geometry("500x500")
    info["bg"]='#FF8087'
    info.title("Información personal")
    fontStylelbl = tkFont.Font(family='Open Sans Light', size='30', weight='bold')
    lbl1=tk.Label(info, text="Pablo Josué Barahona Luncey", font=fontStylelbl, bg="#FF8087", fg="#222831").place(x=25, y=25)
    lbl2=tk.Label(info, text="202109715", font=fontStylelbl, bg="#FF8087", fg="#222831").place(x=25, y=75)
    lbl3=tk.Label(info, text="3560855890101", font=fontStylelbl, bg="#FF8087", fg="#222831").place(x=25, y=125)
    lbl4=tk.Label(info, text="Lenguajes Formales y Programación B-", font=fontStylelbl, bg="#FF8087", fg="#222831").place(x=25, y=175)




#---------------------------------------------------
#---------------------------------------------------



#Ventana 1 (Inicio)
inicio = tk.Tk()
inicio.title("Proyecto 1")
inicio["bg"]="#222831"
inicio.geometry("1160x735")


#labels and buttons
cuadro = tk.Text(inicio, width=126, height=31, font=('Open Sans Light', 10), fg="#000000", bg="#FF8087")
cuadro.place(x=250, y=210)
lblincial = tk.Label(inicio, width=138, height=3, font=('Open Sans Light', 10), fg="#FF8087", bg="#FF8087").place(x=25, y=140)
panellateral = tk.Label(inicio, width=25, height=31, font=('Open Sans Light', 10), fg="#FF8087", bg="#FF8087").place(x=25, y=210)
#cuadro = tk.Label(inicio, width=110, height=31, font=('Open Sans Light', 10), fg="#000000", bg="#FF8087").place(x=250, y=210) 
fontStyle= tkFont.Font(family='Open Sans Light', size='30', weight='bold')

fontStylebttn = tkFont.Font(family='Open Sans Light', size='14', weight='bold')
fontStylelbl = tkFont.Font(family='Open Sans Light', size='8')
# cuadrox=tk.Label(inicio, text=("Linea: "), font=fontStylelbl, fg="#DDDDDD", bg="#30475E").place(x=990, y=690)
# cuadroy=tk.Label(inicio, text=("Columna: "), font=fontStylelbl, fg="#DDDDDD", bg="#30475E").place(x=1050, y=690)
lbl1 = tk.Label(inicio, width=46, height=2, text="Compilador", font=fontStyle, fg="#DDDDDD", bg="#30475E").place(x=25, y=25)
bttn_new = tk.Button(inicio, text="Nuevo", width=13, height='2', font=fontStylebttn, command=nuevo, fg="#30475E", bg="#DDDDDD").place(x=45, y=215)
bttn_open_file = tk.Button(inicio, text="Abrir Archivo", width=13, height='2', font=fontStylebttn, command=abrirArchivo, fg="#30475E", bg="#DDDDDD").place(x=45, y=285)
bttn_save = tk.Button(inicio, text="Guardar", width=13,height='2', font=fontStylebttn, command=guardar, fg="#30475E", bg="#DDDDDD").place(x=45, y=355)
bttn_save_as = tk.Button(inicio, text="Guardar como",width=13,height='2', font=fontStylebttn, command=guardarcomo, fg="#30475E", bg="#DDDDDD").place(x=45, y=425)
bttn_analyze = tk.Button(inicio, text="Analizar Archivo",width=13,height='2', font=fontStylebttn, command=analizar, fg="#30475E", bg="#DDDDDD").place(x=45, y=495)
bttn_errors = tk.Button(inicio, text="Ver errores",width=13,height='2', font=fontStylebttn, command=errores, fg="#30475E", bg="#DDDDDD").place(x=45, y=565)
bttn_exit = tk.Button(inicio, text="Salir", width=13,height='2', font=fontStylebttn, command=salirPro, fg="#30475E", bg="#DDDDDD").place(x=45, y=635)
bttn_usermanual = tk.Button(inicio, text="Manual de usuario", width=15, font=fontStylebttn, command=manualusuario, fg="#30475E", bg="#DDDDDD").place(x=260, y=147)
bttn_technicalmanual = tk.Button(inicio, text="Manual Técnico", width=15, font=fontStylebttn, command=manualtecnico, fg="#30475E", bg="#DDDDDD").place(x=500, y=147)
bttn_help = tk.Button(inicio, text="Temas de Ayuda", width=15, font=fontStylebttn, command=info, fg="#30475E", bg="#DDDDDD").place(x=750, y=147)
posx=0
posy=0
def ShowPosition(event):
    pos=cuadro.index(INSERT)
    pos2=pos.split(".")
    posx=pos2[0]
    posy=pos2[1]
    cuadroy=tk.Label(inicio, width=16, text=("Fila: "+posx+ " Columna: "+posy), font=fontStylelbl, fg="#DDDDDD", bg="#30475E").place(x=1000, y=690)
def ShowPosition2(event):
    pos=cuadro.index(INSERT)
    pos2=pos.split(".")
    posx=pos2[0]
    posy=pos2[1]
    cuadroy=tk.Label(inicio, width=16, text=("Fila: "+posx+ " Columna: "+str(int(posy)+1)), font=fontStylelbl, fg="#DDDDDD", bg="#30475E").place(x=1000, y=690)
cuadro.bind('<Button-1>', ShowPosition)
cuadro.bind('<Key>', ShowPosition2)
inicio.mainloop()