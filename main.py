from tkinter import *

#creamos ventana 
window = Tk()
window.config(bg="black", padx=5, pady=5)#cambio el color de la vantana a negro

#variable constante que determina el ancho de los botones de la calculadora
WIDTH_BOTTON=5

#usamos una variable stringvar para almacenar el dato ingresado por el usuario
math_expresion=StringVar()

#variable que va almacenando todos los datos ingresados  por el usuario
user_inseted_data=""

#label que muestra informacion en la pantalla de nuestra calculadora
label_data = Entry(window, textvariable=math_expresion, width=25)
label_data.grid(row=0, columnspan=4)


#Funcion que obtiene toda la data ingresada por el usuario y se almacena en 'user_inserted_data'
#num, es el dato enviado por el usario al hacer click en uno de los botones con valores asignados
def get_data(num): 
    #llamamos a la variable global user_inserted_data
    global user_inseted_data
    user_inseted_data += str(num)
    
    #despues de obtener  la data ingresada por el usuario la asignamos a la variable'math_expresion'
    math_expresion.set(user_inseted_data)


#funcion para realizar, ejecutar el calculo matematico
def calculate():
    #en nuestra calculadora se pueden presentar errores al hacer el calculo, como por ejemplo divisiones por '0'
    #por eso usamos 'try' y 'except'
    try:
        #llamamos a la variable global que contiene nuestra operacion matematica
        global user_inseted_data
    
        #usamos la funcion eval()  que hace calculo matematica de cadenas que representa una expresión matemática
        result=str(eval(user_inseted_data))
        
        #el resultado lo asignamos a la variable 'math_expresion' para que el resultado de la operacion se muestre en pantalla
        #por medio del label 'label_data'
        math_expresion.set(result)
        
        #reiniciamos el valor almacenado en 'user_inserted_data' despues de haber hecho el calculo matematico
        user_inseted_data=''
    except:
        #si aparece algun error
        math_expresion.set("error")
        

#funcion que limpiua la pantalla
def clear():
    global user_inseted_data
    user_inseted_data=''
    math_expresion.set(user_inseted_data)

#CREANDO BOTONES DE SUMA, RESTA, MULTIPLICACION Y DIVISION
button_sum = Button(window,text="+", command=lambda:get_data('+'), width=WIDTH_BOTTON,  bg="dimgray", fg="lightskyblue")
button_sum.grid(row=1, column=3)

button_subtraction = Button(window,text="-", command=lambda:get_data('-'), width=WIDTH_BOTTON, bg="dimgray", fg="lightskyblue")
button_subtraction.grid(row=2, column=3)

button_divide = Button(window,text="/", command=lambda:get_data('/'), width=WIDTH_BOTTON, bg="dimgray", fg="lightskyblue")
button_divide.grid(row=3, column=3)

button_multiply = Button(window,text="*", command=lambda:get_data('*'), width=WIDTH_BOTTON, bg="dimgray", fg="lightskyblue")
button_multiply.grid(row=4, column=3)


#boton de limpiar el contenido de texto en la pantalla
button_suma = Button(window,text="clear", command=clear, width=WIDTH_BOTTON, bg="dimgray", fg="orange")
button_suma.grid(row=4, column=1)

#boton de "=" que seria el boton de calcular
button_equal = Button(window,text="=",  command=calculate, width=WIDTH_BOTTON, bg="dimgray", fg="orange")
button_equal.grid(row=4, column=2)



#CREANDO LOS BOTONES CON LOS NUMEROS  EN NUESTRA CALCULADORA
#NOTE: Se utiliza lambda para crear una función anónima que se ejecuta cuando se presiona el botón, pasando un argumento o parametro
#a la funcion
button_0 = Button(window, text=0,  command=lambda:get_data(0), width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_0.grid(row=4, column=0)

button_1 = Button(window, text=1, command=lambda:get_data(1),  width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_1.grid(row=1, column=0)

button_2= Button(window, text=2, command=lambda:get_data(2),  width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_2.grid(row=1, column=1)

button_3= Button(window, text=3, command=lambda:get_data(3),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_3.grid(row=1, column=2)

button_4= Button(window, text=4, command=lambda:get_data(4),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_4.grid(row=2, column=0)

button_5= Button(window, text=5, command=lambda:get_data(5),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_5.grid(row=2, column=1)

button_6= Button(window, text=6, command=lambda:get_data(6),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_6.grid(row=2, column=2)

button_7= Button(window, text=7, command=lambda:get_data(7),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_7.grid(row=3, column=0)

button_8= Button(window, text=8, command=lambda:get_data(8),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_8.grid(row=3, column=1)

button_9= Button(window, text=9, command=lambda:get_data(9),   width=WIDTH_BOTTON, bg="dimgray", fg="white")
button_9.grid(row=3, column=2)

#bucle infito para mostrar nuesta ventana
window.mainloop()
