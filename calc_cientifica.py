# Importando o Tkinter e o math.
import tkinter as tk
import math

# Configurações do botões;
botao_config = {
    "bg":"#4543d1",
    "fg":"#dde2de",
    "font":("Consolas bold",12),
    "height": "3",
    "width": "10",
    "relief":"flat",
    "activebackground":"#4543d1"
    }

# Digitos especiais;
digitos = ["√","x²","C","sin","cos","tan"]
deg = 1
cnt = 0

# inversa_deg = 1 --> Era para as trigonométricas inversas, mas não pede na questão;

class Calculadora:
    def __init__(self, master):
        self.master = master

        self.displayFrame = tk.Frame(self.master)
        self.displayFrame.pack()

        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()


        self.output = tk.Entry(self.displayFrame,
                               width=36,relief="sunken",bd=3,font=("Consolas bold", 17), fg="#c9c9c5",bg="#4543d1")
        self.output.grid(row=0, column=0)

        # Botões para mudar de RAD para DEG;
        #self.converte = tk.Button(self.displayFrame, botao_config, width = 5, height = 0, text = "DEG", bg="#e35124", command = self.degressRadians)
        #self.converte.grid(row=0, column=1)

        self.criarBotoes()
    # Criando botões;
    def criarBotoes(self):
        self.botoes = [
            ["√","**","(",""],
            ["sin","cos","tan",")"],
            ["7","8","9","-"],
            ["4","5","6","+"],
            ["1","2","3","*"],
            [".","=","C","/"]
            ]
        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes[linha])):
                texto = self.botoes[linha][coluna]

                # lambda x,y : expressao

                b = tk.Button(self.buttonsFrame, botao_config, text = texto, command = lambda x = texto: self.acaoBotoes(x))
                b.grid(row = linha, column = coluna)
    
    # Acão dos botões;
    def acaoBotoes(self,texto):
        global deg
        global inversa_deg
        if texto != "=":
            if texto not in digitos:
                self.output.insert('end', texto)
            else:
                if texto == "√":
                    self.addValor(math.sqrt(float(self.output.get())))
                elif texto == "x²":
                    self.addValor(float(self.output.get() ** 2))
                elif texto == "C":
                    self.addValor("")
                elif texto == "sin":
                    self.addValor(math.sin(float(self.output.get()) * deg))
                elif texto == "cos":
                    self.addValor(math.cos(float(self.output.get()) * deg))
                elif texto == "tan":
                    self.addValor(math.tan(float(self.output.get()) * deg))

        else:
            self.addValor(eval(self.output.get()))

    # Adicionando valores;
    def addValor(self,valor):
        self.output.delete(0, 'end')
        self.output.insert('end', (valor))
    
    def degressRadians(self):
        global deg
        global inversa_deg
        global cnt

        if(cnt == 0):
            deg = math.pi / 180
            inversa_deg = 180 / math.pi
            self.converte['text'] = "RAD"

        else:
            deg = 1
            inversa_deg = 1
            self.converte['text'] = "DEG"
            cnt = 0

# Começando a calc;
raiz = tk.Tk()
Calculadora(raiz)
raiz.mainloop()
