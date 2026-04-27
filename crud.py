import sqlite3

conn = sqlite3.connect("usuarios.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT)""")

conn.commit()

def criar_usuarios():
    nome = input("Qual o seu nome: ")
    email = input("Qual o seu email: ")
    
    cursor.execute("INSERT INTO usuarios (nome,email) VALUES (?,?)",
                   (nome,email))
    conn.commit()
    
    print("Usuario criado!\n")

def listar_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuario cadastrado!\n")
        return
    for usuario in usuarios:
        print(f"ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}")
    print()

def atualizar_usuarios():
    listar_usuarios()
    
    id_usuario = input("Digite o ID do usuário que deseja atualizar: ")
    
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    usuario = cursor.fetchone()
    
    if not usuario:
        print("Usuário não encontrado!\n")
        return
    
    novo_nome = input("Novo nome: ")
    novo_email = input("Novo email: ")

    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE id = ? ",
        (novo_nome,novo_email,id_usuario)
    )
    conn.commit()
    
    print("Usuario atualizado!\n")
    
def deletar_usuarios():
    listar_usuarios()
    
    id_usuario = input("Digite o ID do usuário que deseja deletar: ")
    
    cursor.execute("SELECT * FROM usuarios WHERE id = ?",(id_usuario,))
    usuario = cursor.fetchone()
    
    if not usuario:
        print("Usuário não encontrado!")
        return
    
    confirmar = input("Tem certeza que deseja deletar?? (s/n): ")
    
    if confirmar.lower() != "s":
        print("Operação cancelada.\n")
        return
        
    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (id_usuario,)
    )
    conn.commit()
    print("Usuário deletado!\n")

while True:
    print("""
1 - Criar Usuário
2 - Listar Usuário
3 - Atualizar Usuário
4 - Deletar Usuário
0 - Sair""")

    opcao = input("Qual a sua escolha: ")
    if opcao == "1":
        criar_usuarios()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        atualizar_usuarios()
    elif opcao == "4":
        deletar_usuarios()
    elif opcao == "0":
        break
    else:
        print("Opção invalida!\n")

