# Auto_Pizzas

📖 Manual de Instruções – Pizzaria Digital
🧭 Introdução

Este aplicativo permite que clientes façam login, se cadastrem e realizem pedidos de pizza de forma prática e rápida. Ao final do pedido, o cliente acumula pontos que podem ser usados em futuras compras.
🛠️ Requisitos para uso

    Computador com Python 3 instalado

    Módulos necessários: tkinter, sqlite3, re (já inclusos na maioria das instalações padrão do Python)

    Arquivo do sistema salvo com extensão .py

🚪 Passo a passo para usar o aplicativo
1. Abrir o aplicativo

Execute o arquivo .py com Python. A janela de login será exibida.
2. Cadastro de novo usuário

Se você ainda não tem uma conta:

    Digite um e-mail válido do Gmail (ex: usuario@gmail.com)

    Crie uma senha com no mínimo 6 caracteres

    Clique em Cadastrar

    Uma mensagem de sucesso será exibida

3. Login

Se já possui uma conta:

    Digite seu e-mail e senha

    Clique em Entrar

    Se os dados estiverem corretos, você verá sua pontuação acumulada e será redirecionado para o autoatendimento

4. Realizar um pedido

Na tela de autoatendimento:

    Clique nos itens desejados do cardápio

    Os itens serão adicionados ao seu pedido e exibidos com o valor total

5. Finalizar pedido

    Após escolher os itens, clique em Finalizar Pedido

    Você verá uma mensagem confirmando que sua pizza está sendo preparada

    Seus pontos serão atualizados com base no valor total do pedido

🧾 Informações adicionais

    Cada real gasto equivale a 1 ponto acumulado

    Os pontos são armazenados no banco de dados e exibidos no login

    O sistema salva os dados localmente em usuarios.db

🆘 Dúvidas ou problemas

Caso o aplicativo não abra ou apresente erros:

    Verifique se o Python está instalado corretamente

    Certifique-se de que os módulos tkinter e sqlite3 estão disponíveis

    Confira se o arquivo .py está salvo corretamente





# 🍕 Documentação do Sistema de Autoatendimento - Pizzaria Digital

## 📌 Visão Geral
Este sistema implementa uma interface gráfica para login, cadastro e realização de pedidos em uma pizzaria. Utiliza:

- **Tkinter** para a interface gráfica
- **SQLite** como banco de dados local
- **Regex** para validação de e-mail

---

## 🗃️ Banco de Dados

O banco de dados `usuarios.db` contém uma tabela chamada `usuarios` com os seguintes campos:

| Campo   | Tipo     | Descrição                          |
|---------|----------|------------------------------------|
| id      | INTEGER  | Identificador único (autoincremento) |
| email   | TEXT     | E-mail do usuário (único e obrigatório) |
| senha   | TEXT     | Senha do usuário (obrigatória)     |
| pontos  | INTEGER  | Pontuação acumulada (default: 0)   |

---

## 🌐 Variáveis Globais

- `usuario_logado`: Armazena o e-mail do usuário autenticado
- `pedido`: Lista de itens adicionados ao pedido atual

---

## 🍽️ Cardápio

Dicionário com os itens disponíveis e seus respectivos preços:

```python
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
