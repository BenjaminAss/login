from tkinter import Tk
import tkinter as tk
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import utileri.generic as utl

class Lde:
    
    def prob_ocup(self):

        landa = int(self.landa_entry.get())
        muu = int(self.muu_entry.get())

        min_llegada = landa/60
        min_servicio = muu/60
        p = float(((min_llegada/min_servicio)*100))
        self.pantalla_resultado1.insert(0, p)

    def fun_lq(self):

        landa = int(self.landa_entry.get())
        muu = int(self.muu_entry.get())

        min_llegada = landa/60
        min_servicio = muu/60

        lq = float((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada)))

        self.pantalla_resultado2.insert(0, lq)

    def fun_l(self):

        landa = int(self.landa_entry.get())
        muu = int(self.muu_entry.get())

        min_llegada = landa/60
        min_servicio = muu/60

        l = float((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada))+(min_llegada/min_servicio))

        self.pantalla_resultado3.insert(0, l)

    def fun_wq(self):
        
        landa = int(self.landa_entry.get())
        muu = int(self.muu_entry.get())

        min_llegada = landa/60
        min_servicio = muu/60

        wq = float(((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada)))/min_llegada)

        self.pantalla_resultado4.insert(0, wq)

    def fun_w(self):

        landa = int(self.landa_entry.get())
        muu = int(self.muu_entry.get())

        min_llegada = landa/60
        min_servicio = muu/60

        w = float((((min_llegada*min_llegada)/(min_servicio*(min_servicio-min_llegada)))/min_llegada)+(1/min_servicio))

        self.pantalla_resultado5.insert(0, w)

    def fun_n_ocioso(self):
        
        landa = int(self.landa_entry.get())
        muu = int(self.muu_entry.get())

        min_llegada = landa/60
        min_servicio = muu/60
        n = float(100-(((min_llegada/min_servicio)*100)))
        self.pantalla_resultado6.insert(0, n)

    def fun_ws(self):

        muu = int(self.muu_entry.get())

        min_servicio = muu/60
        ws = float(1/min_servicio)
        self.pantalla_resultado7.insert(0, ws)


    def nuevo_calculo(self):
        self.pantalla_resultado1.delete(0, 1000)
        self.pantalla_resultado2.delete(0, 1000)
        self.pantalla_resultado3.delete(0, 1000)
        self.pantalla_resultado4.delete(0, 1000)
        self.pantalla_resultado5.delete(0, 1000)
        self.pantalla_resultado6.delete(0, 1000)
        self.pantalla_resultado7.delete(0, 1000)
        self.landa_entry.delete(0, 1000)
        self.muu_entry.delete(0,1000)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Modelo de Lineas de Espera")
        self.root.configure(background="#2A2C2C")
        self.root.geometry("900x500")
        self.root.resizable(0,0)

        #LABEL

        self.landa_label = tk.Label(self.root, text="TIEMPO PROMEDIO DE LLEGADAS: ")
        self.landa_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.landa_label.grid(row=1, column=1, padx= 20, pady= 20, sticky="w")

        self.muu_label = tk.Label(self.root, text="TIEMPO PROMEDIO DE SERVICIO: ")
        self.muu_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.muu_label.grid(row=2, column=1,  padx= 20, pady= 20, sticky="w")

        self.lq_label = tk.Label(self.root, text="N° promedio de clientes que se encuentran esperando a ser atendidos --> ")
        self.lq_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.lq_label.grid(row=4, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

        self.l_label = tk.Label(self.root, text="N° promedio de clientes en el sistema --> ")
        self.l_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.l_label.grid(row=5, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

        self.wq_label = tk.Label(self.root, text="Tiempo promedio que un cliente espera a ser atendido --> ")
        self.wq_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.wq_label.grid(row=6, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

        self.w_label = tk.Label(self.root, text="Tiempo promedio que un cliente pasa en el sistema --> ")
        self.w_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.w_label.grid(row=7, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

        self.n_label = tk.Label(self.root, text="Probabilidad de que el sistema este vacío --> ")
        self.n_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.n_label.grid(row=8, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

        self.ws_label = tk.Label(self.root, text="Tiempo de servicio --> ")
        self.ws_label.configure(background="#2A2C2C", foreground="#FFFFFF", relief="groove")
        self.ws_label.grid(row=10, column=0, columnspan=4, padx= 10 , pady= 10 ,sticky="w")

        #ENTRY

        self.mi_landa = tk.IntVar()
        self.landa_entry = tk.Entry(self.root)
        self.landa_entry.configure(background="#FFFFFF")
        self.landa_entry.grid(row=1, column=2, padx= 5, pady= 20, sticky="w")

        self.mi_muu = tk.IntVar()
        self.muu_entry = tk.Entry(self.root)
        self.muu_entry.configure(background="#FFFFFF")
        self.muu_entry.grid(row=2, column=2,  padx= 5, pady= 20, sticky="w")

        #RESULTADO

        self.pantalla_resultado1 = tk.Entry(self.root)
        self.pantalla_resultado1.grid(row=2, column=4)

        self.texto1 = tk.Label(self.root, text="% " + "del tiempo el sistema está ocupado")
        self.texto1.configure(background="#2A2C2C", foreground="#FFFFFF")
        self.texto1.grid(row=2, column=5)

        self.linea1 = tk.Label(self.root, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.linea1.configure(background="#2A2C2C", foreground="#FFFFFF")
        self.linea1.grid(row=3, column=0, columnspan=10)

        self.pantalla_resultado2 = tk.Entry(self.root)
        self.pantalla_resultado2.grid(row=4, column=4)

        self.pantalla_resultado3 = tk.Entry(self.root)
        self.pantalla_resultado3.grid(row=5, column=4)

        self.pantalla_resultado4 = tk.Entry(self.root)
        self.pantalla_resultado4.grid(row=6, column=4)

        self.pantalla_resultado5 = tk.Entry(self.root)
        self.pantalla_resultado5.grid(row=7, column=4)

        self.pantalla_resultado6 = tk.Entry(self.root)
        self.pantalla_resultado6.grid(row=8, column=2)

        self.texto1 = tk.Label(self.root, text="% " + "del tiempo el sistema está vacío")
        self.texto1.configure(background="#2A2C2C", foreground="#FFFFFF")
        self.texto1.grid(row=8, column=4)

        self.linea1 = tk.Label(self.root, text="-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.linea1.configure(background="#2A2C2C", foreground="#FFFFFF")
        self.linea1.grid(row=9, column=0, columnspan=10)

        self.pantalla_resultado7 = tk.Entry(self.root)
        self.pantalla_resultado7.grid(row=10, column=2)

        self.linea1 = tk.Label(self.root, text=" * Todos los valores de tiempo están en minutos y los de numero de clientes (cantidad) en unidades")
        self.linea1.configure(background="#2A2C2C", foreground="#FFFFFF")
        self.linea1.grid(row=11, column=0, columnspan=10, padx= 15 , pady= 15)

        #BOTONES

        self.boton_calcular1 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.prob_ocup)
        self.boton_calcular1.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular1.grid(row=1, column=4)

        self.boton_nuevo = tk.Button(self.root, text="Nuevo", width=10, height=1, command= self.nuevo_calculo)
        self.boton_nuevo.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_nuevo.grid(row=1, column=5)

        self.boton_calcular2 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.fun_lq)
        self.boton_calcular2.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular2.grid(row=4, column=5)

        self.boton_calcular3 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.fun_l)
        self.boton_calcular3.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular3.grid(row=5, column=5)

        self.boton_calcular4 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.fun_wq)
        self.boton_calcular4.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular4.grid(row=6, column=5)

        self.boton_calcular5 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.fun_w)
        self.boton_calcular5.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular5.grid(row=7, column=5)

        self.boton_calcular6 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.fun_n_ocioso)
        self.boton_calcular6.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular6.grid(row=8, column=5)

        self.boton_calcular7 = tk.Button(self.root, text="Calcular", width=10, height=1, command= self.fun_ws)
        self.boton_calcular7.config(font=('Arial',8,'bold'),
            fg = 'white', bg = '#52BE80', 
            cursor = 'hand2', activebackground='#58D68D')
        self.boton_calcular7.grid(row=10, column=5)

        self.root.mainloop()