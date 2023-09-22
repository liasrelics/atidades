import tkinter as tk
from tkinter import messagebox

def selecionar_sim():
    messagebox.showinfo("Resposta", "Você selecionou 'Sim'")

root = tk.Tk()
root.title("Escolha uma opção")

sim_button = tk.Button(root, text="Sim", command=selecionar_sim)
nao_button = tk.Button(root, text="Não", state=tk.DISABLED)

sim_button.pack()
nao_button.pack()

root.mainloop()