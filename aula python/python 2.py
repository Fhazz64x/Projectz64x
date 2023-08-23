class Filme:

    pass

vingadores = Filme()
print(vingadores)

class Filme:
    def __init__(self,nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

vingadores = Filme('vingadores - guerra infinita', 2018,160)
print(f'nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}')


atlanta = Serie('atlanta', 2018, 2)

print(f'nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas:{atlanta.temporadas}')


