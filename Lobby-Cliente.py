#Importar o sqlite3
import sqlite3

#Conectar ao banco + cursor
conn = sqlite3.connect('cliente.db')
cursor = conn.cursor()
print('Bem-vindo ao Sistema!')

#Incrementação de todas as funções
def insert():
    #Conexão e definição do cursor
    conn = sqlite3.connect('cliente.db')
    cursor = conn.cursor()

    #solicitando dados

    print(' ')

    print('Preencha as informações abaixo:')

    print('')

    dado_nome =  (input('Nome: '))
    dado_idade = (int (input('Idade: ')))
    dado_email = (input ('Email: '))
    dados_fone = (int (input ('Telefone: ')))

    #inserir dados
    cursor.execute("""
        INSERT INTO cliente (nome, idade, email, fone)
        VALUES (?, ?, ?, ?)
    """, (dado_nome, dado_idade, dado_email, dados_fone))

    #salvar no bd
    conn.commit()

    #mensagem de sucesso
    print(' ')

    print('Sucesso! O cliente foi adicionado!')

    print(' ')

    conn.close()
    
def delete():
    #Conexão e definição do cursor
    conn = sqlite3.connect('cliente.db')
    cursor = conn.cursor()

    #solicitação de dados
    id_cliente = (int ( input('Informe o ID do cliente que deseja apagar: ')))

    print(' ')

    resposta = (int (input('Tem certeza? (1 = sim // 2 = não')))

    if resposta == 1 :

    #Atualização de dados dados
        cursor.execute("""
            DELETE FROM cliente
            WHERE id = ?
            """, (id_cliente,))


    #salvar no bd
        conn.commit()

    #mensagem de sucesso
        print(' ')

        print('Sucesso! O cliente foi apagado!')

        print(' ')

        conn.close()

    else: 
        print(' ')

        print('Ação cancelada')

        print(' ')

def select():
    #Conexão e definição do cursor
    conn = sqlite3.connect('cliente.db')
    cursor = conn.cursor()

    print('Lista de clientes cadastrados:')

    print(' ')

    cursor.execute("""
        SELECT * FROM cliente;
        """)

    for linha in cursor.fetchall():
        print(linha)

    print(' ')

    conn.close()

def update():
    conn = sqlite3.connect('cliente.db')
    cursor = conn.cursor()
    #solicitação de dados
    id_cliente = (int ( input('Informe o ID do cliente: ')))

    print(' ')

    print('O que você deseja alterar?')

    print(' ')

    escolha_Up = (int(input('Digite: 1 = Alterar o Nome // 2 = Alterar a Idade // 3 = Alterar o Email // 4 = Alterar o Telefone ')))

    print(' ')

    if escolha_Up == 1:
        
        novo_nome = input('Novo nome: ')

        #Atualização de dados dados
        cursor.execute("""
            UPDATE cliente 
             SET nome = ?
             WHERE id = ?
            """, (novo_nome, id_cliente))
    
    elif escolha_Up == 2:
        
        novo_idade = (int ( input('Nova idade: ')))

        #Atualização de dados dados
        cursor.execute("""
            UPDATE cliente 
            SET idade = ?
            WHERE id = ?
            """, (novo_idade, id_cliente))

    elif escolha_Up == 3:

        novo_email = (input('Novo email: '))

            #Atualização de dados dados
        cursor.execute("""
            UPDATE cliente 
            SET email = ?
            WHERE id = ?
            """, ( novo_email, id_cliente))

    elif escolha_Up == 4:
    
        novo_fone = (int ( input('Novo telefone: ')))

        #Atualização de dados dados
        cursor.execute("""
            UPDATE cliente 
            SET fone = ?
            WHERE id = ?
        """, (novo_fone, id_cliente))

    #salvar no bd
    conn.commit()

    #mensagem de sucesso
    print(' ')
    
    print('Sucesso! Os dados foram alterados!')
    conn.close()


loop = 1
while loop == 1:

    print(' ')

    print('Escolha um das opções abaixo:')

    print(' ')

    escolha = (int(input('Digite: 1 = Inserir dados // 2 = alterar dados // 3 = listar cadastrados // 4 = excluir dados // 5 = sair ')))
    
    print(' ')

    if escolha == 1:
        insert()
    elif escolha == 2:
        update()
    elif escolha == 3:
        select()
    elif escolha == 4:
        delete()
    elif escolha == 5:
        print('Obrigado por ultilizar o sistema!')
        break