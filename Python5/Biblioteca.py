class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # O livro começa como disponível

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} ({status})"

class Membro:
    def __init__(self, nome, id_membro):
        self.nome = nome
        self.id_membro = id_membro

    def __str__(self):
        return f"Membro: {self.nome} (ID: {self.id_membro})"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado.")

    def registrar_membro(self, membro):
        self.membros.append(membro)
        print(f"Membro '{membro.nome}' registrado.")

    def listar_livros(self):
        print("\n--- Livros na Biblioteca ---")
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro)
        print("---------------------------")

    def listar_membros(self):
        print("\n--- Membros da Biblioteca ---")
        if not self.membros:
            print("Nenhum membro cadastrado.")
        for membro in self.membros:
            print(membro)
        print("---------------------------")

    def emprestar_livro(self, titulo_livro, id_membro):
        livro_encontrado = None
        membro_encontrado = None

        # Encontrar o livro e o membro
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break
        
        for membro in self.membros:
            if membro.id_membro == id_membro:
                membro_encontrado = membro
                break

        # Lógica de empréstimo
        if not livro_encontrado:
            print(f"Erro: Livro '{titulo_livro}' não encontrado.")
        elif not membro_encontrado:
            print(f"Erro: Membro com ID '{id_membro}' não encontrado.")
        elif not livro_encontrado.disponivel:
            print(f"Erro: O livro '{titulo_livro}' já está emprestado.")
        else:
            livro_encontrado.disponivel = False
            print(f"'{titulo_livro}' foi emprestado para {membro_encontrado.nome}.")

    def devolver_livro(self, titulo_livro):
        livro_encontrado = None
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break

        if not livro_encontrado:
            print(f"Erro: Livro '{titulo_livro}' não encontrado.")
        elif livro_encontrado.disponivel:
            print(f"Erro: O livro '{titulo_livro}' já está disponível.")
        else:
            livro_encontrado.disponivel = True
            print(f"'{titulo_livro}' foi devolvido com sucesso.")

# --- Código de Exemplo para Testar a Biblioteca ---
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Criar e adicionar livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
    livro3 = Livro("1984", "George Orwell")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Criar e registrar membros
    membro1 = Membro("João Silva", 101)
    membro2 = Membro("Maria Souza", 102)

    biblioteca.registrar_membro(membro1)
    biblioteca.registrar_membro(membro2)

    # Listar livros e membros
    biblioteca.listar_livros()
    biblioteca.listar_membros()

    # Simular empréstimos
    print("\n--- Simulação de Empréstimos ---")
    biblioteca.emprestar_livro("1984", 101)
    biblioteca.emprestar_livro("1984", 101) # Tentando emprestar novamente
    biblioteca.emprestar_livro("Dom Casmurro", 999) # Membro inexistente
    biblioteca.emprestar_livro("O Hobbit", 102) # Livro inexistente

    # Listar livros novamente para ver a mudança de status
    biblioteca.listar_livros()

    # Simular devolução
    print("\n--- Simulação de Devolução ---")
    biblioteca.devolver_livro("1984")
    biblioteca.devolver_livro("1984") # Tentando devolver novamente

    # Listar livros para ver o status atualizado
    biblioteca.listar_livros()