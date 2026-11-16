import sqlite3
from datatime import datetime

conexao=sqlite3.connect('Banco.db')
cursor=conexao.cursor()

cursor.execute("""CREATE TABLE faturamento(
                  id INTEGER PRIMARY KEY AUTOINCREMNT 
                  Convenio TEXT NOT NULl,
                  Tabela_Honorarios TEXT NOT NULL,
                  Tabela_Medicamentos TEXT NOT NULL,
                  Tabela_Materiais TEXT NOT NULL,
                  Fisioterapia_Andares INTEGER NOT NULL,
                  Fisioterapia_Uti INTEGER NOT NULL,
                  Fonoaudiologia INTEGER NOT NULL,
                  Data DATE NOT NULL)""")
cursor.commit()

def convenio():
    while True:
        convenio=input("Digite o nome do convênio a ser cadastrado: ")
        
        if convenio.replance(" "," ").isalpha():
            return convenio
        else:
            print("Nome invalido")
            
def honorarios():
    while True:
        tabela_honorarios=input("Digite a tabela de honorários medicos  acordada: ")
        
        if tabela_horarios.replance(" "," ").isalpha():
           return tabela_honorarios
        else:
            print("Digite uma tabela valida")

def medicamentos():
    while True:
        tabela_medicamentos=input("Digite a tabela de medicamentos acordado: ")
        
        if tabela_medicamentos.replance(" "," ").isalpha():
             return tabela_medicamentos()
        else:
            print("Digite uma tabela valida")

def materiais():
    while True:
        tabela_materiais=input("Digite a tabela de materiais acordado: )
        if tabela_materiais.replance(" "," ").isalpha():
            return tabela_materiais
        else:
          print("Digite uma tabela valida")

def fisioterapia_clinica():
    while True:
        try:
            fisioterapia_clinica= int(input("Qual a quantidade permitida de cobrança de consulta fisioterapia unidade de internação ?"))
            return fisioterapia_clinica
        except ValuesError:
            print("Digite apenas numeros")
            
def fisioterapia_uti():
    try:
        fisioterapia_uti=int(input("Qual a quantidade permitida de cobrança de consulta fisioterapia na UTI adulto /UTI neo ?"))
        return fisioterapia_uti
    except ValuesError:
        print("Digite apenas numeros")
        
def fono():
    try:
       consulta_fono=int(input("Qual a quantida permitida de cobrança consulta com fonoaudióloga por dia ? "))
       return consulta_fono
    except:
        print("Digite apenas numeros")
        
def data():
    return datetime.now().strftime("%d/m/y")
    
Faturamento=[]


   
        
        
    
            
        
    
          
         
            
        
                 
  
















