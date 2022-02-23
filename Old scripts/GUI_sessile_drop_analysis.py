# -*- coding: utf-8 -*-
"""
GUI for sessile drop analysis. Uses contact_angle_analysis_function.py, which in turn uses edge_detection.py.

"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
class StartPage(tk.Tk):
    def __init__(self):
        ####################################### Atributos
        super().__init__()
        self.cadenas=("Theta left","Theta right","Volume","Left speed","Right speed")
        self.cantidadDePixeles=0
        self.salidaCada=0
        self.pixelSize=0
        self.frameRateOfSource=0
        self.fasterExecution=0
        self.queGraficoEnX=0
        self.escalaLogEnX=0
        self.queGraficoEnY=0
        self.escalaLogEnY=0
        
        self.LARGE_FONT= ("Verdana", 12)
        self.SMALL_FONT= ("Verdana", 8)
        self.root = Tk()
        self.root.grid()
        
        self.label1=ttk.Label(self.root, text="File analysis")#Crea una etiqueta label1
        self.label1.grid(row=0, column=1,pady=10,padx=10)#Posiciona la etiqueta detro del formulario
        
        self.labelk=ttk.Label(self.root, text="Amount of pixels from the baseline to fit:", font=self.SMALL_FONT)
        self.labelk.grid(row=1, column=1)
        self.kinput=ttk.Entry(self.root)
        self.kinput.grid(row=2, column=1)
        self.kinput.insert(0, 70)

        self.labelII = ttk.Label(self.root, text="Show output every 'x' frames:", font=self.SMALL_FONT)
        self.labelII.grid(row=3, column=1)
        self.IIinput=ttk.Entry(self.root)
        self.IIinput.grid(row=4, column=1)
        self.IIinput.insert(0, 5)
        
        self.labelpxscale = ttk.Label(self.root, text="Pixel size in mm per pixel:", font=self.SMALL_FONT)
        self.labelpxscale.grid(row=5, column=1)
        self.pxscaleinput=ttk.Entry(self.root)
        self.pxscaleinput.grid(row=6, column=1)
        self.pxscaleinput.insert(0, 1)
        
        self.labelfps = ttk.Label(self.root, text="Framerate of source", font=self.SMALL_FONT)
        self.labelfps.grid(row=7, column=1)
        self.fpsinput=ttk.Entry(self.root)
        self.fpsinput.grid(row=8, column=1)
        self.fpsinput.insert(0, 1)
        
        self.flag1=tk.BooleanVar(self.root,0)#Variable de Control para el checkbox
        checkbox1 = ttk.Checkbutton(self.root,text="Faster execution (but less precise)",variable=self.flag1)
        checkbox1.grid(row=9, column=1)
        
        self.var = tk.IntVar(self.root, 0) # control variable
        for i in range(0,5):
            tk.Radiobutton(self.root, text=self.cadenas[i], value=i, variable=self.var).grid(row=i+1,column=2,pady=2,padx=5)
        
        tk.Button(self.root, text='Go', command=lambda: self.establecerEntradas()).grid(row=10,column=2,pady=10,padx=10)
        
        label2 = ttk.Label(self.root, text="Plot x variable", font=self.LARGE_FONT)
        label2.grid(row=0,column=2,pady=10,padx=10)
        
        self.logxbool = tk.BooleanVar(self.root,0)
        checkbox2 = ttk.Checkbutton(self.root,text="Logaritmic scale",variable=self.logxbool)
        checkbox2.grid(row=6, column=2)  

        label3 = ttk.Label(self.root, text="Plot y variable", font=self.LARGE_FONT)
        label3.grid(row=0,column=3,pady=10,padx=10)

        self.typeyplot=tk.IntVar(self.root,0) 
        for i in range(0,5):
            tk.Radiobutton(self.root, text=self.cadenas[i], value=i, variable=self.typeyplot).grid(row=i+1,column=3,pady=2,padx=5)
                    
        self.logybool = tk.BooleanVar(self.root,0)
        checkbox2 = ttk.Checkbutton(self.root,text="Logaritmic scale",variable=self.logybool)
        checkbox2.grid(row=6, column=3)  
    #********************Metodos GET Y SET personalizados    
    def establecerEntradas(self):
        self.cantidadDePixeles=self.kinput.get()
        self.salidaCada=self.IIinput.get()
        self.pixelSize=self.pxscaleinput.get()
        self.frameRateOfSource=self.fpsinput.get()
        self.fasterExecution=self.flag1.get()
        self.queGraficoEnX=self.var.get()
        self.escalaLogEnX=self.logxbool.get()
        self.queGraficoEnY=self.typeyplot.get()
        self.escalaLogEnY=self.logybool.get()
        self.root.destroy()
 
    def getcantidadDePixeles(self):
        return self.cantidadDePixeles
    def getSalidaCada(self):
        return self.salidaCada
    def getPixelSize(self):
        return self.pixelSize
    def getFrameRateOfSource (self):
        return self.frameRateOfSource
    def getFasterExecution(self):
        return self.fasterExecution
    def getQueGraficoEnX(self):
        return self.queGraficoEnX
    def getEscalaLogEnX(self):
        return self.escalaLogEnX
    def getQueGraficoEnY(self):
        return self.queGraficoEnY
    def getEscalaLogEnY(self):
        return self.escalaLogEnY
    def imprimirParametrosDeEntrada(self):
        print("Amount of pixels from the baseline to fit:")
        print(self.cantidadDePixeles)
        print("Show output every 'x' frames:")
        print(self.salidaCada)
        print("Pixel size in mm per pixel:")
        print(self.pixelSize)
        print("Framerate of source")
        print(self.frameRateOfSource)
        print("Faster execution (but less precise)")
        print(self.fasterExecution)
        print("Plot x variable")
        print(str(self.queGraficoEnX) +" :"+ str(self.cadenas[self.queGraficoEnX]))
        print("Escala Logaritmica en el eje X")
        print(self.escalaLogEnX)
        print("Plot y variable")
        print(str(self.queGraficoEnY )+" :"+ str(self.cadenas[self.queGraficoEnY]))
        print("Escala Logaritmica en el eje Y")
        print(self.escalaLogEnY)
#****************************************FIN DE LA CLASE StarPage*******************************************

#Para testear la clase StarPage, se usan las siguientes 4 lineas de codigo, pero cuando  ejecute el programa completo, se deben comentarizar        
ventana=StartPage() 
ventana.root.mainloop()
print("Los parametros ingresados por el usuario, se almacenan como atributos de la clase, que posteriormente usaré")
ventana.imprimirParametrosDeEntrada()
