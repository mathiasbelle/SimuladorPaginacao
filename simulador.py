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

        self.tamanhosPagina = ["8","16","32","64","128"]
        self.tamanhosPaginaStrings = StringVar(master)
        self.tamanhosPaginaStrings.set(self.tamanhosPagina[1])
        self.tamanhosPaginaMenu = OptionMenu(self.container, self.tamanhosPaginaStrings, *self.tamanhosPagina)
        self.tamanhosPaginaMenu.pack()

        self.tamanhoPaginaLabel = Label(self.container, text = "Selecione o tamanho da memória", font = self.fontePadrao)
        self.tamanhoPaginaLabel.pack()

        self.tamanhosMemoria = ["512","1024","2048","4096"]
        self.tamanhosMemoriaStrings = StringVar(master)
        self.tamanhosMemoriaStrings.set(self.tamanhosMemoria[1])
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
        tempoTotal = 1
        tempoEspera = 0
        tempoProcessos = 1
        cond = True
        lol = 0
        print("tempo | processo | posicao_inicial_na_memoria | ação")
        input()
        while(cond):
            #print("Quantidade de processos dentro: ",len(processosDentro))
            print("Quantidade de páginas disponíveis: ",qtdPaginas)
            #print("TEMPO TOTAL: ", contadorTempo, "\nQuantidade de páginas disponíveis: ",qtdPaginas)
            #input()
            #print("\n TEMPO: ", contadorTempo)
            cond2 = True
            #x = 0
            while(cond2):
                #print("Contador tempo: ", contadorTempo)
                #print("x = ",x,"\nContador tempo: ", contadorTempo, "\nQuantidade de páginas: ",qtdPaginas)
                #print("TEMPO: ", contadorTempo, "\nQuantidade de páginas: ",qtdPaginas)
                #print("Processo atual = ", self.listaProcessos[0].ID)
                #print("\nID: ",self.listaProcessos[0].ID,"\nT_CRIADO: ",self.listaProcessos[0].T_CRIADO,"\nT_MORTO: ",self.listaProcessos[0].T_MORTO,"\nTAMANHO: ",self.listaProcessos[0].TAMANHO)
                #if(self.listaProcessos[0].T_CRIADO <= tempoTotal): #and self.listaProcessos[0].qtd_paginas <= qtdPaginas
                    #print("ID: ",self.listaProcessos[0].ID,"\nT_CRIADO: ",self.listaProcessos[0].T_CRIADO,"\nT_MORTO: ",self.listaProcessos[0].T_MORTO,"\nTAMANHO: ",self.listaProcessos[0].TAMANHO)
                if(self.listaProcessos[0].qtd_paginas <= qtdPaginas and self.listaProcessos[0].T_CRIADO <= tempoProcessos):
                    #print("TEMPO TOTAL: ", contadorTempo, "\nQuantidade de páginas disponíveis: ",qtdPaginas)
                    #print("Tempo processos: ", tempoProcessos)
                    #print("ID: ",self.listaProcessos[0].ID,"\nT_CRIADO: ",self.listaProcessos[0].T_CRIADO)#"\nT_MORTO: ",self.listaProcessos[0].T_MORTO,"\nTAMANHO: ",self.listaProcessos[0].TAMANHO)
                    #print("Processo ID ",self.listaProcessos[0].ID," entrou.")
                    if(lol == 1):
                        tempoProcessos+=1
                    print("Tempo quando entrou: ",tempoTotal," Processo: ",self.listaProcessos[0].ID," NULL"," Entrou")
                    if(self.listaProcessos[0].T_CRIADO == self.listaProcessos[0].T_MORTO):
                        print("Tempo quando saiu: ",tempoTotal," Processo: ",self.listaProcessos[0].ID," NULL","|| Saiu")
                        self.listaProcessos.pop(0)
                    else:
                        qtdPaginas -= self.listaProcessos[0].qtd_paginas
                        processosDentro.append(self.listaProcessos.pop(0))
                    #contadorTempo+=1
                    lol = 1
                    if(self.listaProcessos[0].T_CRIADO > tempoProcessos):
                        #print("Processo pular:",self.listaProcessos[0].ID)
                        while(self.listaProcessos[0].T_CRIADO != tempoProcessos):
                            tempoProcessos+=1
                            #print("Tempo = ",tempoProcessos)
                        lol = 0
                        break
                    #tempoProcessos+=1
                    #tempoEspera = 0
                    #print("Quantidade de processos dentro: ",len(processosDentro))
                else:
                    #print("Tempo processos: ", tempoProcessos)
                    #print("Sem espaço para o processo ",self.listaProcessos[0].ID,", processo esperando.")
                    #print("Tempo de espera: ",tempoEspera)
                    print("Tempo: ",tempoTotal," Processo: ",self.listaProcessos[0].ID," NULL"," Esperando", "||Tempo processos: ",tempoProcessos)
                    tempoEspera+=1
                    break
                    #filaEspera.append(self.listaProcessos[0])
                    #contadorTempo+=1
                    #x+=1
                    #print("XX = ",x)
                #else:
                #    cond2 = False
                #x+=1
            tempoTotal = tempoEspera + tempoProcessos
            #print("Tempo total = ", tempoTotal)
            if processosDentro:
                #print("Tempo total = ", tempoTotal)
                #print("Quantidade de processos dentro: ",len(processosDentro))
                #for a in range(len(processosDentro)):
                cond3 = True
                a = 0
                while(cond3):
                    if(a >= len(processosDentro)):
                        break
                    if(processosDentro[a].T_MORTO <= tempoProcessos):
                        qtdPaginas += processosDentro[a].qtd_paginas
                        #print("Tempo de morrer: ", processosDentro[a].T_MORTO,"\ntempoProcessos: ",tempoProcessos)
                        #print("Processo ID = ",processosDentro[a].ID," saiu.")
                        print("Tempo quando saiu: ",tempoTotal," Processo: ",processosDentro[a].ID," NULL","|| Saiu")
                        processosDentro.pop(a)
                        a-=1
                    a+=1 
            #tempoTotal = contadorTempo+tempoEspera
            #contadorTempo+=1

            if not self.listaProcessos and processosDentro:
                cond = False
            
            input()
    
root = Tk()
Aplication(root)
root.mainloop()