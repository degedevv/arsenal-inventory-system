inventario = []

equipamentos = ['Espada', 'Capacete', 'Peitoral', 'Calça']
qualidades = ['Diamante', 'Ferro', 'Ouro']


def verificar_itens(lista, mensagem):
    listar(lista)

    escolha = input(mensagem).capitalize()

    while escolha not in lista:
        print ('Opcão invalida.')
        listar(lista)
        escolha = input('Tente novamente: ').capitalize()
    return escolha



def linha():
    print('\n'+'-=-'*13 + '\n')


def menu():
    print('\n'+'+'+'-=-'*10+'+')
    print('|  -> BEM VINDO AO ARSENAL <-  |')
    print('+'+'-=-'*10+'+'+'\n')


def listar(lista):
    print('Itens disponíveis:\n')
    print('🔸' + '\n🔸'.join(lista)+'\n')


def selecao_itens():
    resposta = 'S'

    while resposta == 'S':

        item = verificar_itens(equipamentos, 'Escolha um item: ')

        print('=-='*20)

        qualidade = verificar_itens(qualidades, 'Escolha uma qualidade: ')

        nomenclatura = item + ' de ' + qualidade
        inventario.append(nomenclatura)

        linha()
        print(f'{nomenclatura} adicionado ao seu inventario✅' + '\n')

        resposta = input('Deseja adicionar mais algum item? [S / N]').upper()
        linha()


def melhorias():
    decisao_melhoria = 'S'

    while decisao_melhoria == 'S':
        decisao_melhoria = input('Deseja melhorar algum item [S/N]? ').upper()

        if decisao_melhoria == "S":
            linha()
            for i, itens in enumerate(inventario, start=1):
                print(f'{i} - {itens} \n')

            try:
                indice = int(input('Selecione qual item deseja melhorar')) - 1

                if indice < 0 or indice >= len(inventario):
                    print('Número inválido.')
                    continue

            except ValueError:
                print('Digite um número: ')
                continue

            item_antes = inventario[indice]

            if 'Ouro' in item_antes:
                item_melhorado = item_antes.replace('Ouro', 'Ferro')
                linha()
                print('Item melhorado com sucesso! ✅\n')

            elif 'Ferro' in item_antes:
                item_melhorado = item_antes.replace('Ferro', 'Diamante')
                linha()
                print('Item melhorado com sucesso! ✅ \n')
            else:
                linha()
                print('Não é possivel melhorar um item de Diamante (nv. MÁXIMO) \n')
                continue

            inventario[indice] = item_melhorado


def conclusao():
    linha()
    print('Seu inventário final ficou assim: ' + '\n ')
    for i, itens in enumerate(inventario, start=1):
        print(f'{i} - {itens}')
    linha()


menu()

selecao_itens()

melhorias()

conclusao()
