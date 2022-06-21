from tkinter import *
import tkinter
from tkinter.font import BOLD
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

class Vista():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Proyecto")
        
        self.ventana.resizable(False,False)
        self.ventana.geometry("700x500")
        self.ventana.iconbitmap("iconos/flash.ico")
        
        self.__flagGrafica=False
        #IMAGENES
        self.micro=PhotoImage(file="iconos/micro.png")
        self.nevera=PhotoImage(file="iconos/fridge.png")
        self.tv=PhotoImage(file="iconos/tv.png")
        self.lavadora=PhotoImage(file="iconos/lavadora.png")
        self.luz=PhotoImage(file="iconos/luz.png")
        self.ducha=PhotoImage(file="iconos/ducha.png")
        self.pc=PhotoImage(file="iconos/pc.png")
        self.xbox=PhotoImage(file="iconos/xbox.png")

        #FRAME
        self.miFrame=Frame(width="700",height="500",bg="#C6F3F2",bd=12,relief="groove",cursor="trek")       
        self.miFrame.pack(fill="both",expand=False)        
        self.miFrame.pack(fill="both",expand="True")        
        self.frameGrafica=Frame(self.miFrame,width="380",height="350",relief="ridge",bd=5)
        self.frameGrafica.grid(row=1,column=5,rowspan=4)        
        
        titulo=Label(self.miFrame,relief="groove",text="Proyecto",bg="#82C2FA",font=("Ink Free",19,BOLD))
        titulo.grid(row=0,column=0,columnspan=9,sticky=EW)
        
        #UBICACION IMAGENES
        self.lblDucha=Label(self.miFrame,image=self.ducha,bg="#C6F3F2")
        self.lblDucha.grid(row=1,column=0)
        self.selectDucha=BooleanVar()
        self.checkDucha=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectDucha,bg="#C6F3F2")
        self.checkDucha.grid(row=1,column=1)
       
        self.lblNevera=Label(self.miFrame,image=self.nevera,bg="#C6F3F2")
        self.lblNevera.grid(row=2,column=0)
        self.selectNevera=BooleanVar()
        self.checkNevera=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectNevera,bg="#C6F3F2")
        self.checkNevera.grid(row=2,column=1)
        
        self.lblLavadora=Label(self.miFrame,image=self.lavadora,bg="#C6F3F2")
        self.lblLavadora.grid(row=3,column=0)
        self.selectLavadora=BooleanVar()
        self.checkLavadora=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectLavadora,bg="#C6F3F2")
        self.checkLavadora.grid(row=3,column=1)

        self.lbLuz=Label(self.miFrame,image=self.luz,bg="#C6F3F2")
        self.lbLuz.grid(row=4,column=0)
        self.selectLuz=BooleanVar()
        self.checkLuz=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectLuz,bg="#C6F3F2")
        self.checkLuz.grid(row=4,column=1)

        self.lblMicro=Label(self.miFrame,image=self.micro,bg="#C6F3F2")
        self.lblMicro.grid(row=1,column=2)
        self.selectMicro=BooleanVar()
        self.checkMicro=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectMicro,bg="#C6F3F2")
        self.checkMicro.grid(row=1,column=3)

        self.lblPc=Label(self.miFrame,image=self.pc,bg="#C6F3F2")
        self.lblPc.grid(row=2,column=2)
        self.selectPc=BooleanVar()
        self.checkPc=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectPc,bg="#C6F3F2")
        self.checkPc.grid(row=2,column=3)

        self.lblTv=Label(self.miFrame,image=self.tv,bg="#C6F3F2")
        self.lblTv.grid(row=3,column=2)
        self.selectTv=BooleanVar()
        self.checkTv=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectTv,bg="#C6F3F2")
        self.checkTv.grid(row=3,column=3)

        self.lblXbox=Label(self.miFrame,image=self.xbox,bg="#C6F3F2")
        self.lblXbox.grid(row=4,column=2)
        self.selectXbox=BooleanVar()
        self.checkXbox=Checkbutton(self.miFrame,text="Sí",font=(10),variable=self.selectXbox,bg="#C6F3F2")
        self.checkXbox.grid(row=4,column=3)

        #CREDITOS
        Label(self.miFrame,text="Anna Maria Sanchez Rojas\n"+
                                "Johand Esteban Castro Rodriguez\n"+
                                "Nestor Pinzon",
                bg="#CF9997",relief="groove",bd=6,
                font=("System",13,BOLD)).grid(row=5,column=0,columnspan=4,rowspan=4,ipadx=30,pady=8)

        self.btnGrafica=Button(self.miFrame,text="Calcular",font=(10),command=self.calcular)
        self.btnGrafica.grid(row=5,column=5)

        #TOTALES
        self.textMes=StringVar()
        self.textMes.set("Consumo Kw por mes: 0.0")
        self.textCosto=StringVar()
        self.textCosto.set("Costo: $0.0")
        
        self.lblTotalMes=Label(self.miFrame,bg="#C6F3F2",textvariable=self.textMes)
        self.lblTotalMes.grid(row=6,column=5)
        self.lblCosto=Label(self.miFrame,bg="#C6F3F2",textvariable=self.textCosto)
        self.lblCosto.grid(row=7,column=5)       

        self.ventana.mainloop()
    
    def calcular(self):
        electro=list()
        hora=list()
        energia=list()
        totalDia=0
        if self.selectDucha.get():
            ducha=[1,12,4,8]
            electro.append(ducha)
        if self.selectLavadora.get():
            lavadora=[2,15,12,17]
            electro.append(lavadora)
        if self.selectLuz.get():
            luz=[1,4,17,24]
            electro.append(luz)
        if self.selectMicro.get():
            micro=[2,20,14,16]
            electro.append(micro)
        if self.selectNevera.get():
            nevera=[10,30,6,13]
            electro.append(nevera)
        if self.selectPc.get():
            pc=[7,45,18,24]
            electro.append(pc)
        if self.selectTv.get():
            tv=[3,9,6,18]
            electro.append(tv)
        if self.selectXbox.get():
            xbox=[4,21,15,20]
            electro.append(xbox)
        
        for i in range(1,25):
            total=0
            for j in electro:                
                if i>=j[2] and i<=j[3]:
                    total=total+j[1]
                else:
                    total=total+j[0]
            totalDia=totalDia+total
            hora.append(i)
            energia.append(total)
            kw=(totalDia/1000 )*30
            self.textMes.set(f"Consumo Kw por mes: {round(kw,2)}")
            self.textCosto.set(f"Costo: ${round(kw*650.57,2)}")
        self.frameGrafica.grid_forget()
        self.frameGrafica=Frame(self.miFrame,width="380",height="350",relief="ridge",bd=5)
        self.frameGrafica.grid(row=1,column=5,rowspan=4)
    
        fig = Figure(figsize=(3.69,2.98),dpi = 100)
        ejes = fig.add_axes((0.15, 0.15, 0.7, 0.7))        
        lienzo = FigureCanvasTkAgg(fig, master = self.frameGrafica)
        lienzo.draw()
        lienzo.get_tk_widget().pack(expand=1)
        toolbar = NavigationToolbar2Tk(lienzo, self.frameGrafica)
        toolbar.update()
        ejes.grid()
        ejes.plot(hora,energia)

Vista()