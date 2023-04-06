from tkinter import *
import tkinter as tk

# pode ser usado o ttk para melhorar a interface e configurar um label na criacao da janela
class MinhaApp: # definindo uma classe
    def __init__(self,root):
        root.title('Projeto')  # Projeto
        root.geometry('500x400')  # tamanho da janela do programa quando abre
        root.maxsize(1200, 800)  # maximizar a janela do programa

        frame = Frame(root, width= 200, height= 100, borderwidth=2, relief='ridge')
        frame.pack(side= tk.RIGHT)


        self.label_text = StringVar()
        label = Label(root, textvariable= self.label_text)
        label['bg'] = 'red'
        label.configure(text='Novo Texto', font=('Arial', 20))
        label.place(x = 150, y = 180)

        self.entry_text = StringVar()
        entry = Entry(root, textvariable= self.entry_text) # alteracoes dos labels em tempo real
        entry.place(x = 100, y = 100)

        # label.configure(textvariable= entry_text) # linka a caixa de dialogo com o primeiro label

        button = Button(root, text= 'Login', command= self.clicar_botao)
        button.pack()

        self.list_item_string = ['Hamburguer,', 'Queijo', 'Pão', 'Bacon', 'Maionese', 'Alface', 'Tomate']
        list_item = StringVar(value= self.list_item_string)
        listbox= Listbox(root,listvariable=list_item)

        listbox['height'] = 5

        listbox.bind('<<ListboxSelect>>', lambda s: self.select_item(s.widget.curselection()))

        listbox.pack()

    def select_item(self, index):
        select_item = self.list_item_string[index[0]]
        self.label_text.set(select_item)


    def clicar_botao(self):
        text = self.entry_text.get()
        self.list_item_string.append(text)
        self.label_text.set(text)



# podemos organizar as caixas de dialogos em forma de celulas como no excel com o grid em todas as janelas(colunas e linhas)



root = Tk()

MinhaApp(root)

root.mainloop()
