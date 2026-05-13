inventario = []

equipamentos = ['ESPADA', 'CAPACETE', 'PEITORAL', 'CALÇA']
qualidades = ['DIAMANTE', 'FERRO', 'OURO']

def linha():
    print('\n'+'-=-'*10 + '\n')

def menu():
    print ('\n'+'+'+'-=-'*10+'+')
    print('|  -> BEM VINDO AO ARSENAL <-  |')
    print ('+'+'-=-'*10+'+'+'\n')

def conclusao():
    print('\n'+ '-=-'*10 + '\n' + 'Seu inventário final ficou assim: ' + '\n' +'-=-'*10)
    for i, itens in enumerate(inventario, start=1):
        print(f'{i} - {itens}')

def selecao_itens():
    resposta = 'S'

    while resposta == 'S':

        print('ITENS QUE VOCÊ PODE ADICIONAR: \n🔸 ESPADA \n🔸 CAPACETE \n🔸 PEITORAL \n🔸 CALÇA \n🔸 BOTAS'+'\n')

        inventario.append(input('Oque deseja levar no inventário? \n'))
        print('=-='*20)

        qualidade = input(
            f'Informe a qualidade da(o) {inventario[-1].capitalize()}: \n🔸 DIAMANTE \n🔸 FERRO \n🔸 OURO \n')

        nomenclatura = inventario[-1].capitalize() + \
            ' de ' + qualidade.capitalize()

        inventario[-1] = nomenclatura
        linha()
        print(f'{inventario[-1]} adicionado ao inventario✅' + '\n')

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

menu()

selecao_itens()

melhorias()

conclusao()
