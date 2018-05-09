from tkinter import *
from tkinter.filedialog import askopenfilename
import math


class Simulacao:
    ID = 0
    T_CRIADO = 0
    T_MORTO = 0
    TAMANHO = 0
    qtd_paginas = 0
'''
def lerArquivo(caminho):
    try:
        arquivo = open(caminho, "r")
    except Exception as ex:
        janela = Tk()
        container = Frame(janela, height = 500)
        container.pack()
        janelaErro = Label(container, text = type(ex), font = 100)
        janelaErro.pack()
        return False
    listaProcessos = []
    
    for lena in arquivo:
        processoAtual = Simulacao()
        linha = lena.split(",")
        processoAtual.ID = int(linha[0])
        processoAtual.T_CRIADO = int(linha[1])
        processoAtual.T_MORTO = int(linha[2])
        processoAtual.TAMANHO = int(linha[3])
        listaProcessos.append(processoAtual)
        
    for x in range(0,len(listaProcessos)):
        print("\nID: ",listaProcessos[x].ID,"\nT_CRIADO: ",listaProcessos[x].T_CRIADO,"\nT_MORTO: ",listaProcessos[x].T_MORTO,"\nTAMANHO: ",listaProcessos[x].TAMANHO)
'''


class Aplication:

    #ID = 0
    #T_CRIADO = 0
    #T_MORTO = 0
    #TAMANHO = 0
    #qtd_paginas = 0
    listaProcessos = []

    def __init__(self, master):
        self.master = master
        self.fontePadrao = ("Arial", "10")
        self.container = Frame(master)
        self.container["height"] = 150
        self.container["width"] = 150
        self.container.pack()

        self.tamanhoPaginaLabel = Label(self.container, text = "Selecione o tamanho da página", font = self.fontePadrao)
        #self.tamanhoPaginaLabel["width"] = 100
        #self.tamanhoPaginaLabel["height"] = 15
        self.tamanhoPaginaLabel.pack()

        self.tamanhosPagina = ["16","32","64","128"]
        self.tamanhosPaginaStrings = StringVar(master)
        self.tamanhosPaginaStrings.set(self.tamanhosPagina[0])
        self.tamanhosPaginaMenu = OptionMenu(self.container, self.tamanhosPaginaStrings, *self.tamanhosPagina)
        self.tamanhosPaginaMenu.pack()

        self.tamanhoPaginaLabel = Label(self.container, text = "Selecione o tamanho da memória", font = self.fontePadrao)
        self.tamanhoPaginaLabel.pack()

        self.tamanhosMemoria = ["128","512","1024","2048"]
        self.tamanhosMemoriaStrings = StringVar(master)
        self.tamanhosMemoriaStrings.set(self.tamanhosMemoria[0])
        self.tamanhosMemoriaMenu = OptionMenu(self.container, self.tamanhosMemoriaStrings, *self.tamanhosMemoria)
        self.tamanhosMemoriaMenu.pack()

        self.label1 = Label(self.container, text = "Selecione o arquivo")
        self.label1.pack()

        self.caminho = Entry(self.container)
       # self.caminho["width"] = 50
        self.caminho.pack(side=LEFT)

        self.filename = Button(self.container, text = "Selecionar arquivo", command = self.openfile)
        self.filename.pack()
        
        self.confirmar = Button(self.container, text = "Começar simulação", command = self.janelaSimulacao )
        self.confirmar.pack()

    def openfile(self):
        self.filename = askopenfilename(title = "Selecionar arquivo",filetypes = (("csv","*.csv"),("txt",".txt"),("all files","*.*"))) 
        print(self.filename)
        self.caminho.delete(0, END)
        self.caminho.insert(0,self.filename)
    
    def lerArquivo(self):
        try:
            arquivo = open(self.caminho.get(), "r")
        except Exception as ex:
            janela = Tk()
            container = Frame(janela, height = 500)
            container.pack()
            janelaErro = Label(container, text = type(ex), font = 100)
            janelaErro.pack()
            return False
        #listaProcessos = []
    
        for lena in arquivo:
            processoAtual = Simulacao()
            linha = lena.split(",")
            processoAtual.ID = int(linha[0])
            processoAtual.T_CRIADO = int(linha[1])
            processoAtual.T_MORTO = int(linha[2])
            processoAtual.TAMANHO = int(linha[3])
            processoAtual.qtd_paginas = math.ceil(processoAtual.TAMANHO/int(self.tamanhosPaginaStrings.get()))

            self.listaProcessos.append(processoAtual)
        
        #for x in range(0,len(self.listaProcessos)):
        #    print("\nID: ",self.listaProcessos[x].ID,"\nT_CRIADO: ",self.listaProcessos[x].T_CRIADO,"\nT_MORTO: ",self.listaProcessos[x].T_MORTO,"\nTAMANHO: ",self.listaProcessos[x].TAMANHO, "\nQtd páginas: ", processoAtual.qtd_paginas)

   # def janelaSimulacao(self):
        #self.master.withdraw()
        #self.newWindow = Toplevel(self.master)
        #self.container2 = Frame(self.master)
        #self.container2.pack()
       # lerArquivo(self.caminho.get())

    def janelaSimulacao(self):
        
        if(self.lerArquivo() == False):
            return
        tamanhoPagina = int(self.tamanhosPaginaStrings.get())
        tamanhoMemoria = int(self.tamanhosMemoriaStrings.get())
        qtdPaginas = tamanhoMemoria / tamanhoPagina
        print("quantidade paginas: ", qtdPaginas)

        janela2 = Tk()

        container2 = Frame(janela2)
        container2.pack()

        logSaidaTitulo = Label(container2, text = "Log Saida")
        logSaidaTitulo.pack()

        logSaida = Label(container2, text = "Vazio")
        logSaida.pack()


        listaLabels = [] # Lista de Labels das paginas

        for x in range(0, int(qtdPaginas)):
            label = Label(container2, text = "Pagina "+str(x)+"\t")
            listaLabels.append(label)
        for x in range(0, len(listaLabels)):
            listaLabels[x].pack(side = LEFT)
        #listaLabels[0]["text"] = listaLabels[0]["text"]+"\nJNDuebfeubUBB"

        # = math.ceil(self.listaProcessos[0].TAMANHO/tamanhoPagina)
        #print("N = ",n)
        processosDentro = []
        #filaEspera = []
        contadorTempo = 1
        tempoEspera = 0
        tempoTotal = 0
        cond = True
        while(cond):
            print("Quantidade de processos dentro: ",len(processosDentro))
            print("TEMPO: ", contadorTempo, "\nQuantidade de páginas disponíveis: ",qtdPaginas)
            input()
            #print("\n TEMPO: ", contadorTempo)
            cond2 = True
            #x = 0
            while(cond2):
                #print("x = ",x,"\nContador tempo: ", contadorTempo, "\nQuantidade de páginas: ",qtdPaginas)
                #print("TEMPO: ", contadorTempo, "\nQuantidade de páginas: ",qtdPaginas)
                #print("Processo atual = ", self.listaProcessos[0].ID)
                #print("\nID: ",self.listaProcessos[0].ID,"\nT_CRIADO: ",self.listaProcessos[0].T_CRIADO,"\nT_MORTO: ",self.listaProcessos[0].T_MORTO,"\nTAMANHO: ",self.listaProcessos[0].TAMANHO)
                if(self.listaProcessos[0].T_CRIADO <= contadorTempo): #and self.listaProcessos[0].qtd_paginas <= qtdPaginas
                    print("\nID: ",self.listaProcessos[0].ID,"\nT_CRIADO: ",self.listaProcessos[0].T_CRIADO,"\nT_MORTO: ",self.listaProcessos[0].T_MORTO,"\nTAMANHO: ",self.listaProcessos[0].TAMANHO)
                    if(self.listaProcessos[0].qtd_paginas <= qtdPaginas):
                        print("Processo ID ",self.listaProcessos[0].ID," entrou.")
                        qtdPaginas -= self.listaProcessos[0].qtd_paginas
                        processosDentro.append(self.listaProcessos.pop(0))
                        contadorTempo+=1
                        tempoEspera = 0
                        #print("Quantidade de processos dentro: ",len(processosDentro))
                    else:
                        print("Sem espaço para o processo ",self.listaProcessos[0].ID,", processo esperando.")
                        print("Tempo de espera: ",tempoEspera)
                        tempoEspera+=1
                        break
                        #filaEspera.append(self.listaProcessos[0])
                    #contadorTempo+=1
                    #x+=1
                    #print("XX = ",x)
                else:
                    cond2 = False
                #x+=1
            if processosDentro:
                print("Tempo total = ", tempoTotal)
                #print("Quantidade de processos dentro: ",len(processosDentro))
                #for a in range(len(processosDentro)):
                cond3 = True
                a = 0
                while(cond3):
                    if(a == len(processosDentro)):
                        break
                    if(processosDentro[a].T_MORTO <= tempoTotal):
                        qtdPaginas += processosDentro[a].qtd_paginas
                        print("Processo ID = ",processosDentro[a].ID," saiu.")
                        processosDentro.pop(a)
                        a-=1
                    a+=1
                        
            tempoTotal = contadorTempo+tempoEspera
            #contadorTempo+=1

            if not self.listaProcessos and processosDentro:
                cond = False
            #input()
    
root = Tk()
Aplication(root)
root.mainloop()