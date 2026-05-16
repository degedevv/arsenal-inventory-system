inventario = []

equipamentos = ['Espada', 'Capacete', 'Peitoral', 'Calça']
qualidades = ['Diamante', 'Ferro', 'Ouro']


def linha():
    print('\n'+'-=-'*10 + '\n')


def menu():
    print('\n'+'+'+'-=-'*10+'+')
    print('|  -> BEM VINDO AO ARSENAL <-  |')
    print('+'+'-=-'*10+'+'+'\n')

def listar(lista):
    print(f'Itens disponíveis:\n🔸{'\n🔸'.join(lista)}')



def selecao_itens():
    resposta = 'S'

    while resposta == 'S':

        listar(equipamentos)
        item = input('O que deseja adicionar ao inventário? \n').capitalize()
        while item not in equipamentos:
            print('Item inválido.')
            listar(equipamentos)
            item = input('Digite novamente: ').capitalize()

        print('=-='*20)

        qualidade = input(f'Informe a qualidade da(o) {item.capitalize()}:')
        listar(qualidades)
        while qualidade not in qualidades:
            print('Qualidade inválida.')
            listar(qualidades)
            qualidade = input('Digite novamente: ').capitalize()

        nomenclatura = item.capitalize() + ' de ' + qualidade.capitalize()
        inventario.append(nomenclatura)

        linha()
        print(f'{nomenclatura} adicionado ao inventario✅' + '\n')

        resposta = input('Deseja adicionar mais algum item? [S / N]').upper()
        linha()


def melhorias():

    decisao_melhoria = 'S'

    while decisao_melhoria == 'S':
        decisao_melhoria = input('Deseja melhorar algum item [S/N]? ').upper()

        if decisao_melhoria == "S":
            linha()
            for i, itens in enumerate(inventario, start=1):
                print(f'{i} - {itens}')

            indice = int(input('Selecicona qual item deseja melhorar: ')) - 1
            item_antes = inventario[indice]

            if 'Ouro' in item_antes:
                item_melhorado = item_antes.replace('Ouro', 'Ferro')
                linha()
                print(f'Item melhorado com sucesso✅')

            elif 'Ferro' in item_antes:
                item_melhorado = item_antes.replace('Ferro', 'Diamante')
                linha()
                print(f'Item melhorado com sucesso✅')
            else:
                linha()
                print('Não é possivel melhorar um item de Diamante (nv MÁXIMO)')
                continue

            inventario[indice] = item_melhorado


def conclusao():
    print('\n' + '-=-'*10 + '\n' +
          'Seu inventário final ficou assim: ' + '\n' + '-=-'*10)
    for i, itens in enumerate(inventario, start=1):
        print(f'{i} - {itens}')


menu()

selecao_itens()

melhorias()

conclusao()
