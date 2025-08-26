class Membro:
    def __init__(self, nome, id_membro, plano):
        self.nome = nome
        self.id_membro = id_membro
        self.plano = plano
        self.aulas_inscritas = []

    def __str__(self):
        return f"Membro: {self.nome} (ID: {self.id_membro}, Plano: {self.plano})"

class Instrutor:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade
        self.agenda = {}  # Formato: {aula: [membro1, membro2, ...]}

    def __str__(self):
        return f"Instrutor(a): {self.nome} - Especialidade: {self.especialidade}"

class Academia:
    def __init__(self, nome_academia):
        self.nome_academia = nome_academia
        self.membros = {}  # Dicionário: {id_membro: objeto_membro}
        self.instrutores = {} # Dicionário: {especialidade: objeto_instrutor}

    def registrar_membro(self, nome, id_membro, plano):
        if id_membro in self.membros:
            print(f"Erro: ID de membro {id_membro} já registrado.")
            return None
        membro = Membro(nome, id_membro, plano)
        self.membros[id_membro] = membro
        print(f"Membro '{nome}' registrado com sucesso.")
        return membro

    def contratar_instrutor(self, nome, especialidade):
        if especialidade in self.instrutores:
            print(f"Aviso: Já existe um instrutor na especialidade '{especialidade}'.")
        instrutor = Instrutor(nome, especialidade)
        self.instrutores[especialidade.lower()] = instrutor
        print(f"Instrutor(a) {nome} contratado(a) na especialidade de {especialidade}.")
        return instrutor

    def agendar_aula(self, especialidade_aula, nome_aula, data_hora):
        instrutor = self.instrutores.get(especialidade_aula.lower())

        if not instrutor:
            print(f"Erro: Especialidade '{especialidade_aula}' não encontrada.")
            return

        nome_completo_aula = f"{nome_aula} em {data_hora}"
        instrutor.agenda[nome_completo_aula] = []
        print(f"Aula de '{nome_aula}' com {instrutor.nome} em {data_hora} agendada.")

    def inscrever_membro_aula(self, id_membro, especialidade_aula, nome_aula, data_hora):
        membro = self.membros.get(id_membro)
        instrutor = self.instrutores.get(especialidade_aula.lower())

        if not membro:
            print(f"Erro: Membro com ID {id_membro} não encontrado.")
            return
        
        if not instrutor:
            print(f"Erro: Instrutor de '{especialidade_aula}' não encontrado.")
            return

        nome_completo_aula = f"{nome_aula} em {data_hora}"
        if nome_completo_aula not in instrutor.agenda:
            print(f"Erro: Aula '{nome_completo_aula}' não encontrada na agenda.")
            return

        instrutor.agenda[nome_completo_aula].append(membro)
        membro.aulas_inscritas.append(nome_completo_aula)

        print(f"Membro '{membro.nome}' inscrito na aula de '{nome_completo_aula}' com sucesso.")

    def listar_alunos_aula(self, especialidade_aula, nome_aula, data_hora):
        instrutor = self.instrutores.get(especialidade_aula.lower())
        
        if not instrutor:
            print(f"Erro: Especialidade '{especialidade_aula}' não encontrada.")
            return

        nome_completo_aula = f"{nome_aula} em {data_hora}"
        if nome_completo_aula not in instrutor.agenda or not instrutor.agenda[nome_completo_aula]:
            print(f"\nNenhum aluno inscrito na aula de '{nome_completo_aula}'.")
            return
        
        print(f"\n--- Alunos na aula de '{nome_completo_aula}' ---")
        for membro in instrutor.agenda[nome_completo_aula]:
            print(f"- {membro}")
        print("--------------------------------------------------")

# --- Código de Exemplo para Testar o Sistema ---
if __name__ == "__main__":
    academia_alpha = Academia("Academia Alpha Fitness")

    # 1. Registrar membros
    academia_alpha.registrar_membro("Pedro Alves", 201, "Mensal")
    academia_alpha.registrar_membro("Juliana Lima", 202, "Anual")

    # 2. Contratar instrutores
    academia_alpha.contratar_instrutor("Ricardo Costa", "Musculação")
    academia_alpha.contratar_instrutor("Fernanda Gomes", "Pilates")

    # 3. Agendar aulas
    academia_alpha.agendar_aula("Musculação", "Treino de Pernas", "Segunda 18:00")
    academia_alpha.agendar_aula("Pilates", "Pilates Avançado", "Quarta 09:00")

    # 4. Inscrever membros nas aulas
    print("\n--- Inscrevendo Membros ---")
    academia_alpha.inscrever_membro_aula(201, "Musculação", "Treino de Pernas", "Segunda 18:00")
    academia_alpha.inscrever_membro_aula(202, "Pilates", "Pilates Avançado", "Quarta 09:00")
    
    # Tentando inscrever em uma aula inexistente
    academia_alpha.inscrever_membro_aula(201, "Yoga", "Yoga Iniciante", "Sexta 10:00") 

    # 5. Listar alunos por aula
    academia_alpha.listar_alunos_aula("Musculação", "Treino de Pernas", "Segunda 18:00")
    academia_alpha.listar_alunos_aula("Pilates", "Pilates Avançado", "Quarta 09:00")