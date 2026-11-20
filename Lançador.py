import sqlite3
from datetime import datetime

conexao=sqlite3.connect('Banco.db')
cursor=conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Faturamento(
                  id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  Convenio TEXT NOT NULL,
                  Tabela_Honorarios TEXT NOT NULL,
                  Tabela_Medicamentos TEXT NOT NULL,
                  Tabela_Materiais TEXT NOT NULL,
                  Fisioterapia_Andares INTEGER NOT NULL,
                  Fisioterapia_Uti INTEGER NOT NULL,
                  Fonoaudiologia INTEGER NOT NULL,
                  Data DATE NOT NULL)""")

conexao.commit()

def convenios():
    while True:
        convenio=input("Digite o nome do convênio a ser cadastrado: ")
        
        if convenio.replace(" ","").isalpha():
            return convenio
        else:
            print("Nome invalido")
            
def honorarios():
    while True:
        tabela_honorarios=input("Digite a tabela de honorários medicos  acordada: ")
        
        if tabela_honorarios.replace(" ","").isalpha():
           return tabela_honorarios
        else:
            print("Digite uma tabela valida")

def medicamentos():
    while True:
        tabela_medicamentos=input("Digite a tabela de medicamentos acordado: ")
        
        if tabela_medicamentos.replace(" ","").isalpha():
             return tabela_medicamentos
        else:
            print("Digite uma tabela valida")

def materiais():
    while True:
        tabela_materiais=input("Digite a tabela de materiais acordado: ")
        if tabela_materiais.replace(" ","").isalpha():
            return tabela_materiais
        else:
          print("Digite uma tabela valida")

def fisioterapia_clinica():
    while True:
        try:
            fisioterapia_clinica= int(input("Qual a quantidade permitida de cobrança de consulta fisioterapia unidade de internação ?"))
            return fisioterapia_clinica
        except ValueError:
            print("Digite apenas numeros")
            
def fisioterapia_uti():
    while True:
      try:
        fisioterapia_uti=int(input("Qual a quantidade permitida de cobrança de consulta fisioterapia na UTI adulto /UTI neo ?"))
        return fisioterapia_uti
      except ValueError:
        print("Digite apenas numeros")
        
def fono():
    while True:
       try:
        consulta_fono=int(input("Qual a quantida permitida de cobrança consulta com fonoaudióloga por dia ? "))
        return consulta_fono
       except:
        print("Digite apenas numeros")
        
def data():
    return datetime.now().strftime("%d/%m/%y")
    
Faturamento=[]

while True:
   
 print("\nCadastrador de Convênios")
 print("1- Para cadastrar informações")
 print("2- Para pesquisar por convênio")
 print("3- Para alterar informação cadastrada")
 print("4- Para acessar todos os convênios cadastrados")
 print("5- Para sair")

 escolha = input("\nDigite qual a opção desejada: ").strip()

 if escolha == '1':

    while True:
        convenio = {}

        convenio['Nome'] = convenios()
        convenio['Honorario'] = honorarios()
        convenio['Tabela_medicamentos'] = medicamentos()
        convenio['Tabela_materiais'] = materiais()
        convenio['Fisio_andares'] = fisioterapia_clinica()
        convenio['Fisio_uti'] = fisioterapia_uti()
        convenio['Fono'] = fono()
        convenio['Data'] = data()

        Faturamento.append(convenio)

        cursor.execute("""INSERT INTO Faturamento(
                            Convenio,
                            Tabela_Honorarios,
                            Tabela_Medicamentos,
                            Tabela_Materiais,
                            Fisioterapia_Andares,
                            Fisioterapia_Uti,
                            Fonoaudiologia,
                            Data)
                          VALUES(?,?,?,?,?,?,?,?)""",

                       (convenio['Nome'],
                        convenio['Honorario'],
                        convenio['Tabela_medicamentos'],
                        convenio['Tabela_materiais'],
                        convenio['Fisio_andares'],
                        convenio['Fisio_uti'],
                        convenio['Fono'],
                        convenio['Data']))

        conexao.commit()

        print("\nCadastro feito com sucesso!!!")

        desejo = input(
            "Deseja continuar cadastrando? S/N: "
        ).strip().lower()

        if desejo == 'n':
            break


 elif escolha == '2':

    while True:

        pesquisa = input(
            "\nDigite o nome do convênio que deseja pesquisar: "
        ).strip().lower()

        cursor.execute("""SELECT * FROM Faturamento
                          WHERE LOWER(Convenio)=?""",
                       (pesquisa,))

        Resultado = cursor.fetchall()

        if Resultado:

            for registro in Resultado:

                print("\n---- CONVÊNIO ----")
                print(f"ID: {registro[0]}")
                print(f"CONVÊNIO: {registro[1]}")
                print(f"TABELA HONORÁRIOS: {registro[2]}")
                print(f"TABELA MEDICAMENTOS: {registro[3]}")
                print(f"TABELA MATERIAIS: {registro[4]}")
                print(f"FISIOTERAPIA ANDARES: {registro[5]}")
                print(f"FISIOTERAPIA UTI: {registro[6]}")
                print(f"FONOAUDIOLOGIA: {registro[7]}")
                print(f"DATA DO CADASTRO: {registro[8]}")
                print("-" * 60)

        else:
            print("\nConvênio não encontrado!")

        desejo = input(
            "\nDeseja pesquisar outro convênio? S/N: "
        ).strip().lower()

        if desejo == 'n':
            break
          
 elif escolha=='3':
      while True:

        nome=input("Digite o nome do  convênio que deseja alterar informações cadastradas ").strip()

        cursor.execute("""SELECT*FROM Faturamento
                          WHERE LOWER(Convenio)=LOWER(?)
                          """,(nome,))
        registros = cursor.fetchall()

        if registros:

         for registro in registros:

          print("\n---- CONVÊNIO ----")
          print(f"ID: {registro[0]}")
          print(f"CONVÊNIO: {registro[1]}")
          print(f"TABELA HONORÁRIOS: {registro[2]}")
          print(f"TABELA MEDICAMENTOS: {registro[3]}")
          print(f"TABELA MATERIAIS: {registro[4]}")
          print(f"FISIOTERAPIA ANDARES: {registro[5]}")
          print(f"FISIOTERAPIA UTI: {registro[6]}")
          print(f"FONOAUDIOLOGIA: {registro[7]}")
          print(f"DATA: {registro[8]}")



       
          
          print("\n----QUAL INFORMAÇÃO DESEJA ALTERAR- ? ---")
          print("1-CONVÊNIO ")
          print("2-TABELA HONORÁRIOS")
          print("3-TABELA MEDICAMENTOS")
          print("4-TABELA MATERIAIS")
          print("5-FISIOTERAPIA ANDARES")
          print("6-FISIOTERAPIA UTI")
          print("5-FONOAUDILOGIA")

        alterador= input("\nDigite a opção selecionada").strip()

        if alterador=="1":
              nova_informacao=convenios()
              nova_data=data()
              campo='Convenio'
              campo2='Data'
             
        elif alterador=="2":
              nova_informacao=honorarios()
              nova_data=data()
              campo='Tabela_Honorarios'
              campo2='Data'

        elif alterador=="3":
              nova_informacao=medicamentos()
              nova_data=data()
              campo='Tabela_Medicamentos'
              campo2='Data'


        elif alterador=="4":
              nova_informacao=materiais()
              nova_data=data()
              campo='Tabela_Materiais' 
              campo2='Data'


        elif alterador=="5":
                nova_informacao=fisioterapia_clinica()
                nova_data=data()
                campo='Fisioterapia_Andares'
                campo2='Data'

        elif alterador=="6":
                nova_informacao=fisioterapia_uti()
                nova_data=data()
                campo='Fisioterapia_Uti'
                campo2='Data'

        elif alterador=="7":
                nova_informacao=fono()
                nova_data=data()
                campo='Fonoaudiologia'
                campo2='Data'
        else:
                print("\nOpção inválida!")
                continue
        
        cursor.execute(f"""UPDATE Faturamento
                              SET {campo}=?,
                                  {campo2}=?
                              WHERE LOWER(Convenio)=?""",
                          (nova_informacao, nova_data, nome.lower()))
        conexao.commit()

        print("\nAlteração realizada com sucesso!")
           
        desejo=input("\nDeseja continuar alterando? S/N: ").strip().lower()

        if desejo=='n':
              break
 
        
 elif escolha == '4':

    cursor.execute("""
        SELECT * FROM Faturamento
        ORDER BY Convenio ASC
    """)

    resultados = cursor.fetchall()

    if resultados:

        print("\n" + "=" * 70)
        print("             RELATÓRIO DE CONVÊNIOS CADASTRADOS")
        print("=" * 70)

        for registro in resultados:

            print(f"""
                      ID: {registro[0]}
                      CONVÊNIO: {registro[1]}
                      TABELA HONORÁRIOS: {registro[2]}
                      TABELA MEDICAMENTOS: {registro[3]}
                      TABELA MATERIAIS: {registro[4]}
                      FISIOTERAPIA ANDARES: {registro[5]}
                      FISIOTERAPIA UTI: {registro[6]}
                      FONOAUDIOLOGIA: {registro[7]}
                      DATA DO CADASTRO: {registro[8]}
                                                     """)

            print("-" * 70)

            print(f"TOTAL DE CONVÊNIOS CADASTRADOS: {len(resultados)}")

    else:
        print("\nNão existem convênios cadastrados!")

 elif escolha == '5':
     print("\nSaindo do programa...")
     break

 conexao.close()

                
        
        
    
            
        
    
          
         
            
        
                 
  
















