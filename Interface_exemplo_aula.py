from tkinter import*
import tkinter as tk

class Tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class AppDeTarefas:
    def __init__(self, root):
        root.title('Cálculo de Salário')
        root.geometry('1280x720')
        frame = Frame(root, borderwidth=2, relief='groove')
        frame.grid (row=1, column=1, sticky = 'N, W, E, S')
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        nome_lista = Label(frame, text='Coisas a fazer:')
        nome_lista.grid(row=1, column=1, sticky = 'W, S')

        self.tarefas_a_fazer = [
            Tarefa('Treino', 'Agachamento, supino, elevações'),
            Tarefa('Limpar a casa', 'Lavar a louça, varrer, passar pano'),
            Tarefa('Estudar', 'Ler o livro, fazer exercícios'),
            Tarefa('Compras', 'Comprar pão, leite, ovos'),
        ]
        self.nomes_das_tarefas = StringVar(value = list(map(lambda x: x.nome, self.tarefas_a_fazer)))
        self.lista_de_tarefas = Listbox(frame, listvariable = self.nomes_das_tarefas)
        self.lista_de_tarefas.bind('<<ListboxSelect>>',lambda s: self.selecionar_tarefa(self.lista_de_tarefas.curselection()))
        self.lista_de_tarefas.grid(row=2, column=1, sticky = 'W, E', rowspan = 5)

        self.descricao_selecionada = StringVar()
        self.descricao_label = Label (frame, textvariable = self.descricao_selecionada, wraplength = 500)
        self.descricao_label.grid(row=7, column=1, sticky = 'W, E')

        #label do nome da tarefa
        cabecalho_tarefa_label = Label(frame, text='Introduza uma nova tarefa:')
        cabecalho_tarefa_label.grid(row=1, column=2, sticky = 'W, S')

        nome_tarefa_label = Label(frame, text='Titulo para a nova tarefa:')
        nome_tarefa_label.grid(row=2, column=2, sticky = 'W, S')

        self.nome = StringVar()
        nome_entry = Entry(frame, textvariable= self.nome)
        nome_entry.grid(row=3, column=2, sticky = 'W, S')

        descricao_tarefa_label = Label(frame, text='Descrição para a nova tarefa:')
        descricao_tarefa_label.grid(row=4, column=2, sticky='W, S')

        self.descricao = StringVar()
        descricao_entry = Entry(frame, textvariable=self.descricao)
        descricao_entry.grid(row=5, column=2, sticky='W, S')

        guardar_botao = Button(frame, text='Guardar', command=self.guardar_tarefa)
        guardar_botao.grid(row=6, column=2)

        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=5)
    def selecionar_tarefa(self, index):
        print('Tarefa selecionada:')
        tarefa_selecionada = self.tarefas_a_fazer[index[0]]
        self.descricao_selecionada.set(tarefa_selecionada.descricao)

    def guardar_tarefa(self):
        nome = self.nome.get()
        descricao = self.descricao.get()
        nova_tarefa = Tarefa(nome, descricao)
        self.tarefas_a_fazer.append(nova_tarefa)
        self.nomes_das_tarefas.set(list(map(lambda x: x.nome, self.tarefas_a_fazer)))


root = Tk()
AppDeTarefas(root)
root.mainloop()
