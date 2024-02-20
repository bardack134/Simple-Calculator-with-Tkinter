from tkinter import *

# Following will import tkinter.ttk module and 
# automatically override all the widgets 
# which are present in tkinter module. 
# from tkinter.ttk import *

#creamos ventana 
window = Tk()
window.config(bg="black")#cambio el color de la vantana a negro

#label que muestra informacion el pantalla
label_data = Label(window, text="", width=25)
label_data.grid(row=0, columnspan=4)

#variable que va guardando el resultado de nuestra operacion matematica
result=0

#variable constante que determina el ancho de los botones de la calculadora
WIDTH_BOTTON=5


data_number=StringVar()

#Los botones de acuerdo a sus nombres llamaran a cualquiera de estas funciones
def number_0():
    num_0=0
    label_data.config(text=num_0)
    return num_0

def number_1():
    num_1=1
    label_data.config(text=num_1)
    return num_1

def number_2():
    num_2=2
    label_data.config(text=num_2)
    return num_2

def number_3():
    num_3=3
    label_data.config(text=num_3)
    return num_3

def number_4():
    num_4=4
    label_data.config(text=num_4)
    return num_4

def number_5():
    num_5=5
    label_data.config(text=num_5)
    return num_5

def number_6():
    num_6=6
    label_data.config(text=num_6)
    return num_6

def number_7():
    num_7=7
    label_data.config(text=num_7)
    return num_7

def number_8():
    num_8=8
    label_data.config(text=num_8)
    return num_8

def number_9():
    num_9=9
    label_data.config(text=num_9)
    return num_9

#FUNCIONES QUE CALCULAN SUMA, RESTA, DIVISION, MULTIPLICACION RESPECTIVAMENTE
def calculate_sum():
    global result
    global calculando
    calculando="sum"
    value=int(label_data.cget("text"))
    result +=value
    print(result)
    return calculando
    
#Funcion que calcula el total de nuestra operacion matematica y la muestra en pantalla        
def total_result():
    if calculando=="sum":
        global result
        value=int(label_data.cget("text"))
        result +=value
        label_data.config(text=result)


#CREANDO BOTONES DE SUMA, RESTA, MULTIPLICACION Y DIVISION
#cada boton llama a　su respectiva funcion que realiza su operacion matematica
button_suma = Button(window,text="+", command=calculate_sum, width=WIDTH_BOTTON,  bg="dimgray", fg="lightskyblue")
button_suma.grid(row=1, column=3)

button_suma = Button(window,text="-", width=WIDTH_BOTTON, bg="dimgray", fg="lightskyblue")
button_suma.grid(row=2, column=3)

button_suma = Button(window,text="*", width=WIDTH_BOTTON, bg="dimgray", fg="lightskyblue")
button_suma.grid(row=3, column=3)

button_suma = Button(window,text="/", width=WIDTH_BOTTON, bg="dimgray", fg="lightskyblue")
button_suma.grid(row=4, column=3)


#boton de limpiar el contenido de texto en la pantalla
button_suma = Button(window,text="clear", width=WIDTH_BOTTON, bg="dimgray", fg="orange")
button_suma.grid(row=4, column=1)

#boton de "=" que seria el boton de calcular
button_suma = Button(window,text="=", command=total_result, width=WIDTH_BOTTON, bg="dimgray", fg="orange")
button_suma.grid(row=4, column=2)


#CREANDO LOS BOTONES DE NUESTRA CALCULADORA
#cada boton llama a una funcion para crear un valor de acuerdo al valor indicado en el boton
button_0 = Button(window, text=0,  command=number_0, width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_0.grid(row=4, column=0)

button_1 = Button(window, text=1, command=number_1,  width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_1.grid(row=1, column=0)

button_2= Button(window, text=2, command=number_2,  width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_2.grid(row=1, column=1)

button_3= Button(window, text=3, command=number_3,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_3.grid(row=1, column=2)

button_4= Button(window, text=4, command=number_4,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_4.grid(row=2, column=0)

button_5= Button(window, text=5, command=number_5,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_5.grid(row=2, column=1)

button_6= Button(window, text=6, command=number_6,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_6.grid(row=2, column=2)

button_7= Button(window, text=7, command=number_7,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_7.grid(row=3, column=0)

button_8= Button(window, text=8, command=number_8,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_8.grid(row=3, column=1)

button_9= Button(window, text=9, command=number_9,   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_9.grid(row=3, column=2)

#bucle infito para mostrar nuesta ventana
window.mainloop()
