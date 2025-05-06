import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Nome dos ficheiros JSON
ficheiros_json = {
    "Selos": "selos.json",
    "Globos de Neve": "globos_de_neve.json",
    "Moedas": "moedas.json"
}

# Carrega os dados a partir de ficheiros JSON
def carregar_dados():
    dados = {"Selos": [], "Globos de Neve": [], "Moedas": []}
    for colecao, ficheiro in ficheiros_json.items():
        if os.path.exists(ficheiro):
            with open(ficheiro, 'r', encoding='utf-8') as f:
                dados[colecao] = json.load(f)
    return dados

# Guarda os dados em ficheiros JSON
def guardar_dados():
    for colecao, itens in colecoes.items():
        with open(ficheiros_json[colecao], 'w', encoding='utf-8') as f:
            json.dump(itens, f, ensure_ascii=False, indent=4)

# Base de dados em memória (carregada de ficheiros JSON)
colecoes = carregar_dados()

# Função para criar janelas específicas para cada coleção
def abrir_janela_colecao(nome_colecao):
    campos = {
        "Selos": ["ID", "País", "Ano", "Tema", "Valor Facial", "Estado", "Observações"],
        "Globos de Neve": ["ID", "Origem", "Tema", "Material", "Altura (cm)", "Ano Aquisição", "Observação"],
        "Moedas": ["ID", "País", "Valor Nominal", "Ano", "Material", "Estado", "Raridade", "Observações"]
    }

    janela = tk.Toplevel()
    janela.title(f"Coleção: {nome_colecao}")
    entradas = {}

    for i, campo in enumerate(campos[nome_colecao]):
        tk.Label(janela, text=campo).grid(row=i, column=0, padx=5, pady=5, sticky='w')
        entrada = tk.Entry(janela, width=40)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[campo] = entrada

    def guardar():
        dados = {campo: entradas[campo].get() for campo in entradas}
        colecoes[nome_colecao].append(dados)
        guardar_dados()
        messagebox.showinfo("Guardado", f"{nome_colecao[:-1]} adicionado com sucesso!")
        for entrada in entradas.values():
            entrada.delete(0, tk.END)

    def ver_registos():
        lista = tk.Toplevel(janela)
        lista.title("Registos Guardados")
        for idx, item in enumerate(colecoes[nome_colecao]):
            tk.Label(lista, text=f"{idx+1}: {item}", anchor="w", justify="left").pack(fill="both", padx=5, pady=2)

    tk.Button(janela, text="Guardar", command=guardar).grid(row=len(campos[nome_colecao]), column=0, pady=10)
    tk.Button(janela, text="Ver Registos", command=ver_registos).grid(row=len(campos[nome_colecao]), column=1, pady=10)

# Janela principal
def janela_principal():
    root = tk.Tk()
    root.title("Gestão de Coleções Pessoais")
    root.geometry("300x250")

    tk.Label(root, text="Selecione uma coleção para gerir:", font=("Arial", 12)).pack(pady=10)

    botoes = ["Selos", "Globos de Neve", "Moedas"]
    for nome in botoes:
        tk.Button(root, text=nome, width=20, command=lambda n=nome: abrir_janela_colecao(n)).pack(pady=5)

    root.mainloop()

janela_principal()
