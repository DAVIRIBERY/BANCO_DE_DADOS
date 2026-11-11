
import sqlite3

conexao = sqlite3.connect("Banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Pratileira(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Atendimento INTEGER NOT NULL,
                   Nome TEXT NOT NULL,
                   Data DATE NOT NULL,
                   Pasta1 TEXT,
                   Pasta2 TEXT,
                   Pasta3 TEXT,
                   Situacao TEXT
)""")

def atendimento():
    return int(input("\nDigite o atendimento: "))

def nome():
    return input("\nDigite o nome: ")

def data_periodo():
    return input("\nDigite a data em que se inicia o periodo da conta: ")

def Pasta1():
    return input("\nDigite a situação da pasta1, RECEBIDA / NAO RECEBIDA: ").strip().upper()

def pasta2():
    return input("\nDigite a situação da pasta2, RECEBIDA / NAO RECEBIDA: ").strip().upper()

def pasta3():
    return input("\nDigite a situação da pasta3, RECEBIDA / NAO RECEBIDA: ").strip().upper()

while True:

    print("\n LANÇADOR DE DADOS: Prateleira do Faturamento")

    Atendimento = atendimento()
    Data = data_periodo()
    NOME = nome()

    PASTA1 = Pasta1()
    PASTA2 = pasta2()
    PASTA3 = pasta3()

    SITUACAO = ""

    if PASTA1 == "RECEBIDA" and PASTA2 == "RECEBIDA" and PASTA3 == "RECEBIDA":
        SITUACAO = "FINALIZADAS"
    else:
        SITUACAO = "PENDENTES"

    cursor.execute("""INSERT INTO Pratileira
                   (Atendimento, Nome, Data, Pasta1, Pasta2, Pasta3, Situacao)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                   (Atendimento, NOME, Data, PASTA1, PASTA2, PASTA3, SITUACAO))

    conexao.commit()

    print("\nCadastro feito com sucesso!!!")
    print("Situação:", SITUACAO)

    desejo = input("\nDeseja continuar cadastrando? S/N: ").strip().lower()

    if desejo == 'n':
        break

conexao.close()

                 
  
