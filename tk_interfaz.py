from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

import cv2
import numpy as np

from dis_euclidiana import distancia_euclidiana

class Aplicacion():
    def __init__(self, r):
        r.title('Mini proyecto')
        r.geometry('400x100')
        barra_menu = Menu(r)
        r.config(menu=barra_menu)

        #------------- ELEMENTOS DE LA BARRA -------------
        parametrico = Menu(barra_menu, tearoff=0)
        r_neuronal = Menu(barra_menu, tearoff=0)
        asociacion = Menu(barra_menu, tearoff=0)

        #------------- ASIGNACIÓN ELEMENTOS DE LA BARRA -------------
        barra_menu.add_cascade(label='BP', menu=parametrico)
        barra_menu.add_cascade(label='RN', menu=r_neuronal)
        barra_menu.add_cascade(label='Asociación', menu=asociacion)

        parametrico.add_command(label='Bayesiano Parámetrico', command=self.algoritmo_BP)

        r_neuronal.add_command(label='Red Neuronal')

        asociacion.add_command(label='Asociación')

        #------------- FRM PINCIPAL -------------
        frm_principal = ttk.Frame(r)
        frm_principal.pack()

        l_instrucciones = ttk.Label(frm_principal, text='Por favor, seleccione un algoritmo para comenzar.')
        l_instrucciones.grid(row=0, column=0, columnspan=3)

        btn_euclidiano = ttk.Button(frm_principal, text='Distancia euclidiana', command=self.algoritmo_BP)
        btn_euclidiano.grid(row=1, column=0)
        btn_red_neuronal = ttk.Button(frm_principal, text='Red neuronal')
        btn_red_neuronal.grid(row=1, column=1)
        btn_asociacion = ttk.Button(frm_principal, text='Asociación')
        btn_asociacion.grid(row=1, column=2)

        for child in frm_principal.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def algoritmo_BP(self):
        nueva_ventana = Tk()
        nueva_ventana.title('Distancia Euclidiana')

        #------------- VARIABLES GLOBALES -------------
        self.dir_img = StringVar()

        frm_principal = ttk.Frame(nueva_ventana)
        frm_principal.pack()

        l_titulo = ttk.Label(
            frm_principal, 
            text="""
                Análisis con el método Bayesiano paramétrico: \n
                Para una distribución normal o distancia Euclidiana (dE)
            """
        )
        l_titulo.grid(row=0, column=0, columnspan=2)

        l_red = ttk.Label(frm_principal, text="R:")
        l_red.grid(row=1, column=0)
        l_green = ttk.Label(frm_principal, text="G:")
        l_green.grid(row=2, column=0)
        l_blue = ttk.Label(frm_principal, text="B:")
        l_blue.grid(row=3, column=0)

        self.e_red = ttk.Entry(frm_principal, justify='center')
        self.e_red.grid(row=1, column=1)
        self.e_green = ttk.Entry(frm_principal, justify='center')
        self.e_green.grid(row=2, column=1)
        self.e_blue = ttk.Entry(frm_principal, justify='center')
        self.e_blue.grid(row=3, column=1)

        #------------- BOTONES -------------
        btn_euc_manual = ttk.Button(frm_principal, text='Patrón digitado', command=self.evento_manual)
        btn_euc_manual.grid(row=5, column=0)

        btn_euclidiano = ttk.Button(frm_principal, text='Desde imagen', command=self.abrir_imagen)
        btn_euclidiano.grid(row=5, column=1)

        for child in frm_principal.winfo_children():
            child.grid_configure(padx=5, pady=5)

        nueva_ventana.mainloop()

    def abrir_imagen(self):
        try:
            archivo = filedialog.askopenfilename(
                title="Seleccionar imagen", 
                filetypes=(("PNG", "*.png"), ("JPG", "*.jpg"), ("JPEG", "*.jpeg"))
            )

            self.dir_img = archivo

            self.trabajar_imagen()
        except:
            messagebox.showerror('Error', 'No se seleccionó ninguna imagen.')

    def clasificar(self, patron):
        clase_asignada = ""

        d_c1 = distancia_euclidiana(patron, (203, 212, 218))
        d_c2 = distancia_euclidiana(patron, (102, 92, 41))
        d_c3 = distancia_euclidiana(patron, (181, 146, 109))

        if d_c1 > d_c2 > d_c3 or d_c2 > d_c1 > d_c3:
            clase_asignada = "El patrón pertenece a la clase C3"
        elif d_c1 > d_c3 > d_c2 or d_c3 > d_c1 > d_c2:
            clase_asignada = "El patrón pertenece a la clase C2"
        elif d_c3 > d_c2 > d_c1 or d_c2 > d_c3 > d_c1:
            clase_asignada = "El patrón pertenece a la clase C1"

        return clase_asignada

    def evento_manual(self):
        try:
            red = float(self.e_red.get())
            green = float(self.e_green.get())
            blue = float(self.e_blue.get())

            patron = np.array( (red, green, blue) )

            clase = self.clasificar(patron)

            messagebox.showinfo(
                'Clasificación',
                clase
            )
        except:
            messagebox.showerror('Error de valor', 'Ingrese un valor válido RGB.')

    def m_event(self, event, x, y, flags, params):
        # Evento con mouse, descomentar uno de los dos
        #if event == cv2.EVENT_MOUSEMOVE:

        # Evento con clic
        if event == cv2.EVENT_LBUTTONDOWN:
            b = self.img[y, x, 0]
            g = self.img[y, x, 1]
            r = self.img[y, x, 2]
            print(r, g, b)

            patron = np.array( (r, g, b) )

            print(self.clasificar(patron))
            
            cv2.imshow('image', self.img)

    def trabajar_imagen(self):
        self.img = cv2.imread(self.dir_img, 1)
    
        cv2.imshow('image', self.img)
    
        cv2.setMouseCallback('image', self.m_event)
    
        cv2.waitKey(0)
    
        cv2.destroyAllWindows()

#-----------------MAIN--------------
raiz = Tk()
Aplicacion(raiz)
raiz.mainloop()