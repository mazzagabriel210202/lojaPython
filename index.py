print('''
      Faça sua escolha:
          1: Fazer login
          2: Adicionar produto
          3: Fechar pedido
          4: Sair
      ''')

escolha = int(input("Escolha uma opção: "))

carrinho = {}  # Dicionário para armazenar os produtos no carrinho e suas quantidades

match escolha:
    case 1:
        print("Fazendo login")
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        
        match len(senha):
            case senha_len if senha_len < 5:
                raise ValueError("Sua senha deve ter mais de 5 caracteres")
            case _:
                print("Seja bem-vindo,", nome)
    
    case 2:
        print("Adicionando produto")
        
        produtos = {
            'produtoA': 200,
            'produtoB': 300,
            'produtoC': 400,
            'produtoD': 500,
            'produtoE': 600,
        }   
        print("Produtos disponíveis:")
        for produto, preco in produtos.items():
            print(f"{produto}: R${preco}")
        
        produto_escolhido = input("Escolha o produto a adicionar: ")
        if produto_escolhido in produtos:
            quantidade = int(input("Digite a quantidade desejada: "))
            if produto_escolhido in carrinho:
                carrinho[produto_escolhido] += quantidade
            else:
                carrinho[produto_escolhido] = quantidade
            print(f"{quantidade}x '{produto_escolhido}' adicionado(s) ao carrinho.")
        else:
            print("Produto não encontrado.")

    case 3:
        print("Fechando pedido")
        total_pedido = sum(produtos[produto] * quantidade for produto, quantidade in carrinho.items())
        print(f"Total a ser pago: R${total_pedido:.2f}")

        # Verificar se o frete é grátis
        if total_pedido >= 100:
            print("Frete grátis!")
        else:
            total_pedido *= 1.20  # Aplicar taxa de frete
            print(f"Total com frete (20%): R${total_pedido:.2f}")

    case 4:
        print("Saindo")














