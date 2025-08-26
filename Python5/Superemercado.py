class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f} (Estoque: {self.estoque})"

class CarrinhoDeCompras:
    def __init__(self):
        self.itens = {} # Dicionário: {nome_produto: quantidade}
        self.valor_total = 0.0

    def adicionar_item(self, produto, quantidade):
        if produto.nome in self.itens:
            self.itens[produto.nome] += quantidade
        else:
            self.itens[produto.nome] = quantidade
        self.valor_total += produto.preco * quantidade
        print(f"{quantidade}x '{produto.nome}' adicionado ao carrinho.")

    def exibir_carrinho(self):
        print("\n--- Itens no Carrinho ---")
        if not self.itens:
            print("O carrinho está vazio.")
        for nome, quantidade in self.itens.items():
            print(f"- {quantidade}x {nome}")
        print(f"------------------------\nTotal: R$ {self.valor_total:.2f}")
        print("------------------------")

class Supermercado:
    def __init__(self, nome):
        self.nome = nome
        self.estoque = {} # Dicionário: {nome_produto: objeto_produto}
    
    def adicionar_produto(self, nome, preco, estoque):
        produto = Produto(nome, preco, estoque)
        self.estoque[nome.lower()] = produto
        print(f"Produto '{nome}' adicionado ao estoque.")

    def exibir_estoque(self):
        print(f"\n--- Estoque do {self.nome} ---")
        if not self.estoque:
            print("O estoque está vazio.")
        for produto in self.estoque.values():
            print(produto)
        print("------------------------------")
    
    def vender_produtos(self, carrinho):
        print(f"\n--- Finalizando Compra ---")
        sucesso = True
        
        # 1. Verificar estoque antes de vender
        for nome_item, quantidade_desejada in carrinho.itens.items():
            produto = self.estoque.get(nome_item.lower())
            if not produto or produto.estoque < quantidade_desejada:
                print(f"Erro: Quantidade insuficiente de '{nome_item}'.")
                sucesso = False
                break
        
        # 2. Se o estoque for suficiente, processar a venda
        if sucesso:
            for nome_item, quantidade_desejada in carrinho.itens.items():
                produto = self.estoque.get(nome_item.lower())
                produto.estoque -= quantidade_desejada
            
            print("Compra finalizada com sucesso!")
            carrinho.exibir_carrinho()
            return True
        else:
            print("A compra não pôde ser processada devido a falta de estoque.")
            return False

# --- Código de Exemplo para Testar o Sistema ---
if __name__ == "__main__":
    meu_supermercado = Supermercado("Supermercado Python")

    # Adicionar produtos ao estoque
    meu_supermercado.adicionar_produto("Arroz", 12.50, 50)
    meu_supermercado.adicionar_produto("Feijão", 8.90, 30)
    meu_supermercado.adicionar_produto("Leite", 5.00, 100)
    meu_supermercado.adicionar_produto("Pão de Forma", 7.20, 20)

    # Exibir o estoque inicial
    meu_supermercado.exibir_estoque()

    # Criar um carrinho e adicionar itens
    carrinho_cliente = CarrinhoDeCompras()
    carrinho_cliente.adicionar_item(meu_supermercado.estoque["arroz"], 2)
    carrinho_cliente.adicionar_item(meu_supermercado.estoque["leite"], 3)
    carrinho_cliente.adicionar_item(meu_supermercado.estoque["pão de forma"], 1)

    # Exibir o carrinho antes de finalizar a compra
    carrinho_cliente.exibir_carrinho()

    # Tentar finalizar a compra (deve ter sucesso)
    meu_supermercado.vender_produtos(carrinho_cliente)

    # Exibir o estoque após a compra
    meu_supermercado.exibir_estoque()

    # Simular uma nova compra com item fora do estoque
    carrinho_cliente2 = CarrinhoDeCompras()
    carrinho_cliente2.adicionar_item(meu_supermercado.estoque["arroz"], 50) # Excede o estoque
    meu_supermercado.vender_produtos(carrinho_cliente2)