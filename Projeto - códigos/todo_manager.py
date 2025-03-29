# 📂 Arquivo: `todo_manager.py`
import sqlite3
from datetime import datetime

# Criar/conectar ao banco de dados
conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

# Criar tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT NOT NULL,
    categoria TEXT,
    data_criacao TEXT,
    concluida INTEGER DEFAULT 0
)
''')
conn.commit()

def adicionar_tarefa():
    """Adiciona uma nova tarefa ao banco de dados"""
    tarefa = input("\n📝 Nova tarefa: ")
    categoria = input("🏷️ Categoria: ")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    cursor.execute(
        "INSERT INTO tarefas (tarefa, categoria, data_criacao) VALUES (?, ?, ?)",
        (tarefa, categoria, data)
    )
    conn.commit()
    print("✅ Tarefa adicionada!")

def listar_tarefas():
    """Lista todas as tarefas não concluídas"""
    cursor.execute("SELECT * FROM tarefas WHERE concluida = 0")
    tarefas = cursor.fetchall()
    
    print("\n📋 Lista de Tarefas Pendentes:")
    for tarefa in tarefas:
        print(f"""
        ID: {tarefa[0]}
        Tarefa: {tarefa[1]}
        Categoria: {tarefa[2]}
        Data: {tarefa[3]}
        """)

def marcar_concluida():
    """Marca uma tarefa como concluída"""
    listar_tarefas()
    id_tarefa = input("\n🔢 ID da tarefa concluída: ")
    
    cursor.execute(
        "UPDATE tarefas SET concluida = 1 WHERE id = ?",
        (id_tarefa,)
    )
    conn.commit()
    print("🎉 Tarefa marcada como concluída!")

def menu():
    """Exibe o menu interativo"""
    while True:
        print("\n" + "="*30)
        print("📌 GERENCIADOR DE TAREFAS")
        print("="*30)
        print("1. ➕ Adicionar tarefa")
        print("2. 📜 Listar tarefas")
        print("3. ✅ Marcar como concluída")
        print("4. 🚪 Sair")
        
        opcao = input("\n🔹 Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            print("👋 Até logo!")
            break
        else:
            print("⚠️ Opção inválida!")

if __name__ == "__main__":
    menu()
    conn.close()