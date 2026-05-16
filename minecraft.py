inventario = []

equipamentos = ['Espada', 'Capacete', 'Peitoral', 'Calça']
qualidades = ['Diamante', 'Ferro', 'Ouro']


def linha():
    print('\n'+'-=-'*13 + '\n')


def menu():
    print('\n'+'+'+'-=-'*10+'+')
    print('|  -> BEM VINDO AO ARSENAL <-  |')
    print('+'+'-=-'*10+'+'+'\n')


def listar(lista):
    print(f'Itens disponíveis:\n \n🔸{'\n🔸'.join(lista)} \n')


def selecao_itens():
    resposta = 'S'

    while resposta == 'S':

        listar(equipamentos)
        item = input('O que deseja adicionar ao seu inventário? \n').capitalize()
        while item not in equipamentos:
            print('Item inválido.')
            listar(equipamentos)
            item = input('Digite novamente: ').capitalize()

        print('=-='*20)

        listar(qualidades)
        qualidade = input(f'Informe a qualidade da(o) {item}: ').capitalize()
        while qualidade not in qualidades:
            print('Qualidade inválida.')
            listar(qualidades)
            qualidade = input('Digite novamente: ').capitalize()

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

            indice = int(input('Selecicona qual item deseja melhorar: ')) - 1
            item_antes = inventario[indice]

            if 'Ouro' in item_antes:
                item_melhorado = item_antes.replace('Ouro', 'Ferro')
                linha()
                print(f'Item melhorado com sucesso! ✅\n')

            elif 'Ferro' in item_antes:
                item_melhorado = item_antes.replace('Ferro', 'Diamante')
                linha()
                print(f'Item melhorado com sucesso! ✅ \n')
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
