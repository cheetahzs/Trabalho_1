class TelaCategoria:
    def tela_opcoes(self):
        print("-------- CATEGORIA ----------")
        print("1 - Incluir Categoria")
        print("2 - Alterar Categoria")
        print("3 - Listar Categoria")
        print("4 - Excluir Categoria")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_dados_categoria(self):
        print("-------- DADOS CATEGORIA ----------")
        nome = input("Nome: ")
        return {"nome": nome}
    
    def mostra_categoria(self, dados_categoria):
        print("CATEGORIA: ", dados_categoria["nome"])

    def seleciona_categoria(self):
        categoria = input("Categoria a ser selecionada: ")
        return categoria
    
    def mostra_mensagem(self, msg):
        print(msg)