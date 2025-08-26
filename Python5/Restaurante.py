class ItemMenu:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome}: R$ {self.preco:.2f}"

class Pedido:
    def __init__(self):
        self.itens = []
        self.total = 0.0

    def adicionar_item(self, item_menu):
        self.itens.append(item_menu)
        self.total += item_menu.preco
        print(f"'{item_menu.nome}' adicionado ao pedido.")

    def __str__(self):
        descricao_pedido = "--- Detalhes do Pedido ---\n"
        for item in self.itens:
            descricao_pedido += f"- {item.nome} (R$ {item.preco:.2f})\n"
        descricao_pedido += f"\nTotal: R$ {self.total:.2f}"
        return descricao_pedido

class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.menu = {}
        self.pedidos = []

    def adicionar_item_menu(self, nome, preco):
        item = ItemMenu(nome, preco)
        self.menu[nome.lower()] = item
        print(f"'{nome}' adicionado ao menu.")

    def exibir_menu(self):
        print(f"\n--- Menu do {self.nome} ---")
        if not self.menu:
            print("O menu está vazio.")
        for item in self.menu.values():
            print(item)
        print("---------------------------")

    def fazer_pedido(self, itens_pedido):
        novo_pedido = Pedido()
        for item_nome in itens_pedido:
            item = self.menu.get(item_nome.lower())
            if item:
                novo_pedido.adicionar_item(item)
            else:
                print(f"Aviso: '{item_nome}' não está no menu e não foi adicionado ao pedido.")
        
        self.pedidos.append(novo_pedido)
        print("\nPedido finalizado!")
        print(novo_pedido)
        return novo_pedido

    def exibir_historico_pedidos(self):
        print(f"\n--- Histórico de Pedidos do {self.nome} ---")
        if not self.pedidos:
            print("Nenhum pedido foi feito ainda.")
        
        for i, pedido in enumerate(self.pedidos):
            print(f"\nPedido #{i+1}")
            print(pedido)
            print("-" * 25)

        print("------------------------------------------")

# --- Código de Exemplo para Testar o Sistema ---
if __name__ == "__main__":
    restaurante = Restaurante("Cantinho do Sabor")

    # Adicionar itens ao menu
    restaurante.adicionar_item_menu("Pizza Marguerita", 35.00)
    restaurante.adicionar_item_menu("Hamburguer Artesanal", 28.50)
    restaurante.adicionar_item_menu("Refrigerante", 6.00)
    restaurante.adicionar_item_menu("Suco Natural", 8.50)

    # Exibir o menu completo
    restaurante.exibir_menu()

    # Simular o primeiro pedido
    print("\n--- Cliente 1 Fazendo um Pedido ---")
    pedido1 = ["Pizza Marguerita", "Refrigerante", "Batata Frita"] # Batata Frita não existe no menu
    restaurante.fazer_pedido(pedido1)

    # Simular o segundo pedido
    print("\n--- Cliente 2 Fazendo um Pedido ---")
    pedido2 = ["Hamburguer Artesanal", "Suco Natural", "Hamburguer Artesanal"] # Pedindo dois hamburgueres
    restaurante.fazer_pedido(pedido2)

    # Exibir o histórico de todos os pedidos feitos
    restaurante.exibir_historico_pedidos()