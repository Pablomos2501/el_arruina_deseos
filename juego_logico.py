#diccionario={"a":"negro","b":"loca","c":"ella"}
from tkinter import *
from tkinter import messagebox
#variables del carro
carro="carro"
funcional="funcional"
motor="con motor"
nuevo="nuevo"
#variables del videojuego
videojuego="videojuego"
consola="consola"
rayado="rayado"
nuevo="nuevo"
digital="digital"
pc="para pc"


def desear():
    if respuesta.get()=="carro" and complemento.get()=="funcional":
        messagebox.showinfo("TACHAN", f"concedido tendras el {respuesta.get()} que deseas perfectamente {complemento.get()} ... ya saquese ")
    elif respuesta.get()=="carro" and complemento.get()=="con motor":
        messagebox.showinfo("TACHAN", f"concedido tendras un {respuesta.get()} aun asi el {complemento.get()} te explotara en la cara y moriras")
    elif respuesta.get()=="carro" and complemento.get()=="nuevo":
         messagebox.showinfo("TACHAN", f"concedido tendras un {respuesta.get()}  {complemento.get()} espero te guste el rosado")
    elif respuesta.get()=="carro" or complemento.get()=="":
        messagebox.showinfo("XD", f"felicidades aqui esta tu carro sin motor es super viejo y ademas no funciona")  
    #juegos
    elif respuesta.get()=="videojuego" and complemento.get()=="nuevo":
        messagebox.showinfo("TACHAN", f"concedido tienes el  {respuesta.get()}  {complemento.get()} que deseas ")
    elif respuesta.get()=="videojuego" and complemento.get()=="digital":
        messagebox.showinfo("TACHAN", f"concedido tu  {respuesta.get()}  {complemento.get()} se a instalado pero con un virus que arruino tu consola y TV")    
    elif respuesta.get()=="videojuego" and complemento.get()=="para pc":
        messagebox.showinfo("TACHAN", f"concedido tu  {respuesta.get()}  {complemento.get()} se a instalado pero cada vez que lo juegas se escuha el audio de los gemidos a todo volumen")
    elif respuesta.get()=="videojuego" or complemento.get()=="":
         messagebox.showinfo("XD", f"felicidades aqui esta viedeojuego pero esta tan viejo y usado ni si quiera es digital y mucho menos para pc")
    #novia
    elif respuesta.get()=="novia" and complemento.get()=="mujer":
        messagebox.showinfo("TACHAN", f"concedido has encontrado a la  {complemento.get()} que deseas ")
    
    else:
        messagebox.showinfo("Heey", f"como no deseas nada nadie e desea a ti")

juego=Tk()
juego.geometry("700x500+100+100")
juego.title("El Arruina Deseos ")

lbl=Label(text="puedes perdir un deseo").pack()
lbl1=Label(text="pero ojo solo puedes pedir tu deseo con las siguientes palabras").place(x=10,y=40)
lbl2=Label(text="auto, "+"videojuego, "+"novia.").place(x=10,y=60)
lbl3=Label(text="Pero para que deberas se haga realidad tienes que complemetnarlo pero solo puedes especificarlo con una palabra").place(x=10,y=90)

lbl5=Label(text="Deseo un/a").place(x=10,y=160)
respuesta=StringVar()
texbox1=Entry(juego,textvariable=respuesta).place(x=90,y=160)

lbl6=Label(text="con que lo complementaras ").place(x=10,y=190)
complemento=StringVar()
texbox2=Entry(juego,textvariable=complemento).place(x=170,y=190)

boton=Button(juego,text="pedir deseo ",command=desear).place(x=10,y=210)

juego.mainloop()

""" ______     ______     __   __     ______      ______     ______     ______   ______     __  __        ______   __  __     ______        ______     ______     ______  
/\  ___\   /\  __ \   /\ "-.\ \   /\__  _\    /\  ___\   /\  __ \   /\__  _\ /\  ___\   /\ \_\ \      /\__  _\ /\ \_\ \   /\  ___\      /\  == \   /\  __ \   /\__  _\ 
\ \ \____  \ \  __ \  \ \ \-.  \  \/_/\ \/    \ \ \____  \ \  __ \  \/_/\ \/ \ \ \____  \ \  __ \     \/_/\ \/ \ \  __ \  \ \  __\      \ \  __<   \ \  __ \  \/_/\ \/ 
 \ \_____\  \ \_\ \_\  \ \_\\"\_\    \ \_\     \ \_____\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\       \ \_\  \ \_\ \_\  \ \_____\     \ \_\ \_\  \ \_\ \_\    \ \_\ 
  \/_____/   \/_/\/_/   \/_/ \/_/     \/_/      \/_____/   \/_/\/_/     \/_/   \/_____/   \/_/\/_/        \/_/   \/_/\/_/   \/_____/      \/_/ /_/   \/_/\/_/     \/_/ 
"""                                                                                                                                                                       
