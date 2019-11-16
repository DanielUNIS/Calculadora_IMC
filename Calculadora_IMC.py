import tkinter as tk
from tkinter import messagebox

STANDARD_FONT = ("Arial",10)
HEADER_FONT = ("Arial",11)
STANDARD_BOX_SIZE = 20

class IMC(tk.Frame):

    def __init__(self,master=None):
        #Inheritance of Tk and its constructor
        super().__init__(master)
        self.master= master
        self.grid(row=0,column=0)
        #Blocking the user interferance on window size
        self.master.resizable(width=False, height=False)
        self.create_widgets()   

    def create_widgets(self):
        #Declaration
        #Labels
        self.winfo_toplevel().title("Cálculo do IMC - Índice de Massa Corporal")
        self.lb_empty = tk.Label(self, text=" ", font=HEADER_FONT)
        self.lb_name = tk.Label(self, text="Nome do Paciente", font=STANDARD_FONT)
        self.lb_address = tk.Label(self, text="Endereço Completo", font=STANDARD_FONT)
        self.lb_height = tk.Label(self, text="Altura (cm)", font=STANDARD_FONT)
        self.lb_weight = tk.Label(self, text="Peso (kg)", font=STANDARD_FONT)
        self.lb_IMC_result = tk.Label(self, text="-", font=STANDARD_FONT, width=STANDARD_BOX_SIZE, borderwidth=1, relief="solid")
        #Entry Points
        self.et_name = tk.Entry(self, width=STANDARD_BOX_SIZE)
        self.et_address = tk.Entry(self, width=STANDARD_BOX_SIZE)
        self.et_height = tk.Entry(self, width=STANDARD_BOX_SIZE)
        self.et_weight = tk.Entry(self, width=STANDARD_BOX_SIZE)
        #Buttons
        self.bt_calculate = tk.Button(self, text="Calcular", command=self.return_IMC, width=STANDARD_BOX_SIZE)
        self.bt_restart = tk.Button(self, text="Reiniciar", command=self.restart, width=STANDARD_BOX_SIZE)
        self.bt_exit = tk.Button(self, text ="Sair", command=self.exit, width=STANDARD_BOX_SIZE)
        
        #Placing
        #Labels
        self.lb_empty.grid(row=0, column=0, sticky="WESN", columnspan=2)
        self.lb_name.grid(row=2, column=0)
        self.lb_address.grid(row=3, column=0)
        self.lb_height.grid(row=4,column=0)
        self.lb_weight.grid(row=5, column=0)
        self.lb_IMC_result.grid(row=4,column=2,rowspan=2,columnspan=4,sticky="WESN",padx=10)
        #Entry Points
        self.et_name.grid(row=2,column=1, columnspan=4, sticky="WE",pady=10)
        self.et_address.grid(row=3,column=1, columnspan=4, sticky="WE",pady=10)
        self.et_height.grid(row=4,column=1,sticky="WN",pady=10)
        self.et_weight.grid(row=5, column=1,sticky="WN",pady=10)
        #Buttons
        self.bt_calculate.grid(row=7, column=1, sticky="E")
        self.bt_restart.grid(row=7, column=2, sticky="E")
        self.bt_exit.grid(row=7,column=4, sticky="E",padx=10,pady=10)
                          
    def return_IMC(self):
        #This functions returns the IMC with its description.
        calculated_IMC = self.calculate()
        answer = str(calculated_IMC) + ", "
        if calculated_IMC == -1:
            tk.messagebox.showwarning("Erro","Valor(es) inserido(s) inválido(s), tente novamente")
            self.lb_IMC_result["text"]= "-"
            return
        elif calculated_IMC < 18.50:
            answer = answer + "abaixo do peso"
        elif calculated_IMC < 25.00:
            answer = answer + "peso normal"
        elif calculated_IMC < 30.00:
            answer = answer + "sobrepeso"
        elif calculated_IMC < 35.00:
            answer = answer + "obesidade grau 1"
        elif calculated_IMC < 40.00:
            answer = answer + "obesidade grau 2"
        else:
            answer = answer + "obesidade grau 3"

        self.lb_IMC_result["text"]= answer
        
    def calculate(self):
        #This function returns the IMC value, using height in centimeters and
        #weight in kilograms, rounding to 2 decimal cases.
        #If a non integer value is informed, it returns -1.
        if (str(self.et_weight.get()).isnumeric() and
           str(self.et_height.get()).isnumeric()):
               calculated_IMC = (int(self.et_weight.get())/(int(self.et_height.get())/100)**2)   
               return round(calculated_IMC,2)
        else:
            return -1

    def restart(self):
        self.et_name.delete(0,'end')
        self.et_address.delete(0,'end')
        self.et_height.delete(0,'end')
        self.et_weight.delete(0,'end')
        self.lb_IMC_result["text"]= "-"

    def exit(self):
        root.destroy();
        
root = tk.Tk()
app = IMC(root)
app.mainloop()

