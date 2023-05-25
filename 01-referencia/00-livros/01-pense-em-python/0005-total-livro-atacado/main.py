preco_livro = 24.95
qtd_livros = 60
custo_transporte = 3
custo_transporte_adicional = 0.75
preco_total_pessoa = preco_livro*60+custo_transporte+custo_transporte_adicional*(qtd_livros-1)
print(preco_total_pessoa)
print(preco_total_pessoa - preco_total_pessoa * 0.40)