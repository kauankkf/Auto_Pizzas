import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Banco de dados
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL,
        pontos INTEGER DEFAULT 0
    )
""")
conn.commit()

# Variáveis globais
usuario_logado = None
pedido = []

# Cardápio
cardapio = {
    "Pizza Margherita": 35.00,
    "Pizza Calabresa": 38.00,
    "Pizza Quatro Queijos": 42.00,
    "Pizza Frango com Catupiry": 40.00,
    "Borda Recheada": 8.00,
    "Refrigerante 2L": 10.00,
    "Suco Natural": 7.00,
    "Água": 5.00
}

# Funções
def validar_email(email):
    return re.match(r"[^@]+@gmail\.com$", email)

def cadastrar_usuario():
    email = entry_email.get()
    senha = entry_senha.get()
    if not validar_email(email):
        messagebox.showerror("Erro", "Use um e-mail válido do Gmail.")
        return
    if len(senha) < 6:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
        return
    try:
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, senha))
        conn.commit()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Este e-mail já está cadastrado.")

def login_usuario():
    email = entry_email.get()
    senha = entry_senha.get()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    resultado = cursor.fetchone()
    if resultado:
        global usuario_logado
        usuario_logado = email
        pontos = resultado[3]
        messagebox.showinfo("Login", f"Bem-vindo, {email}!\nVocê tem {pontos} pontos acumulados.")
        janela.destroy()
        iniciar_autoatendimento()
    else:
        messagebox.showerror("Erro", "E-mail ou senha incorretos.")

def adicionar_item(item):
    pedido.append(item)
    atualizar_pedido()

def atualizar_pedido():
    texto = ""
    total = 0
    for item in pedido:
        texto += f"{item} - R$ {cardapio[item]:.2f}\n"
        total += cardapio[item]
    texto += f"\nTotal: R$ {total:.2f}"
    lbl_pedido.config(text=texto)

def finalizar_pedido():
    if not pedido:
        messagebox.showwarning("Pedido vazio", "Adicione itens antes de finalizar.")
    else:
        total = sum(cardapio[item] for item in pedido)
        pontos_ganhos = int(total)
        cursor.execute("UPDATE usuarios SET pontos = pontos + ? WHERE email = ?", (pontos_ganhos, usuario_logado))
        conn.commit()
        messagebox.showinfo("Pedido Finalizado", f"Sua pizza está sendo preparada!\nVocê ganhou {pontos_ganhos} pontos.")
        pedido.clear()
        atualizar_pedido()

def iniciar_autoatendimento():
    atendimento = tk.Tk()
    atendimento.title("🍕 Pizzaria Digital")
    atendimento.geometry("450x600")
    atendimento.configure(bg="#fff8f0")

    tk.Label(atendimento, text="🍕 Bem-vindo à Pizzaria Digital", font=("Arial", 16, "bold"), bg="#fff8f0", fg="#d35400").pack(pady=10)

    frame_menu = tk.Frame(atendimento, bg="#fff8f0")
    frame_menu.pack()

    tk.Label(frame_menu, text="Escolha seus itens:", font=("Arial", 12, "bold"), bg="#fff8f0", fg="#2c3e50").pack(pady=5)

    for item in cardapio:
        btn = tk.Button(frame_menu, text=f"{item} - R$ {cardapio[item]:.2f}", width=30,
                        font=("Arial", 10), bg="#f0f0f0", fg="#2c3e50",
                        activebackground="#ffe6cc", command=lambda i=item: adicionar_item(i))
        btn.pack(pady=3)

    tk.Label(atendimento, text="Seu Pedido:", font=("Arial", 12, "bold"), bg="#fff8f0", fg="#2c3e50").pack(pady=10)
    global lbl_pedido
    lbl_pedido = tk.Label(atendimento, text="", justify="left", font=("Arial", 10), bg="#fff8f0", fg="#34495e")
    lbl_pedido.pack()

    btn_finalizar = tk.Button(atendimento, text="Finalizar Pedido", bg="#e74c3c", fg="white",
                              font=("Arial", 12, "bold"), width=25, command=finalizar_pedido)
    btn_finalizar.pack(pady=20)

    atendimento.mainloop()

# Interface de login
janela = tk.Tk()
janela.title("Login - Pizzaria")
janela.geometry("320x280")
janela.configure(bg="#fefefe")

tk.Label(janela, text="🍕 Login da Pizzaria", font=("Arial", 16, "bold"), bg="#fefefe", fg="#c0392b").pack(pady=10)

frame_login = tk.Frame(janela, bg="#fefefe")
frame_login.pack()

tk.Label(frame_login, text="E-mail (Gmail):", font=("Arial", 11), bg="#fefefe").pack()
entry_email = tk.Entry(frame_login, width=30, font=("Arial", 10))
entry_email.pack(pady=5)

tk.Label(frame_login, text="Senha:", font=("Arial", 11), bg="#fefefe").pack()
entry_senha = tk.Entry(frame_login, show="*", width=30, font=("Arial", 10))
entry_senha.pack(pady=5)

tk.Button(janela, text="Entrar", command=login_usuario, width=15, font=("Arial", 11),
          bg="#27ae60", fg="white", activebackground="#2ecc71").pack(pady=5)
tk.Button(janela, text="Cadastrar", command=cadastrar_usuario, width=15, font=("Arial", 11),
          bg="#2980b9", fg="white", activebackground="#3498db").pack()

janela.mainloop()
