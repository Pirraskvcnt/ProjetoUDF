# ==============================================================================
# FUNÇÕES
# ==============================================================================

def cadastrar_dados():
    materia = input("Digite a matéria: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    freq = int(input("Digite a frequência em porcentagem: "))
    return materia, n1, n2, n3, freq


def calcular_nota(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def verificar_frequencia(freq):
    return freq >= 75


def gerar_relatorio(historico):
    print('\n=========================================')
    print('      RELATÓRIO FINAL DO SEMESTRE        ')
    print('=========================================')
    
    total_materias = len(historico)
    aprovados = 0
    soma_medias = 0

    for m in historico:
        soma_medias += m['media']
        if m['status'] == 'Aprovado':
            aprovados += 1
        print(f"-> {m['nome']}: Média {m['media']:.1f} | Frequência: {m['frequencia']}% | Status: {m['status']}")

    media_geral = soma_medias / total_materias if total_materias > 0 else 0
    reprovados = total_materias - aprovados

    print('-----------------------------------------')
    print(f'Total de matérias cursadas: {total_materias}')
    print(f'Matérias aprovadas: {aprovados}')
    print(f'Matérias reprovadas: {reprovados}')
    print(f'Média geral do aluno: {media_geral:.1f}')
    print('=========================================')

# ==============================================================================
# FLUXO PRINCIPAL
# ==============================================================================

historico_materias = []

while True:
    
    materia, n1, n2, n3, freq = cadastrar_dados()

    res = calcular_nota(n1, n2, n3)
    
    freq_ok = verificar_frequencia(freq)
    
    print('-----------------------------------------')
    print(f'A média das notas inseridas é {res:.1f}.')

    if res >= 6 and freq_ok:
        print('Você foi Aprovado')
        apv = 'Aprovado'
    elif not freq_ok and res <= 6:
        print('Reprovado (por falta e por nota)')
        apv = 'Reprovado'
    elif not freq_ok:
        print('Reprovado (por falta)')
        apv = 'Reprovado'
    else:
        print('Reprovado (por nota)')
        apv = 'Reprovado'

    print('-----------------------------------------')
    print('RESUMO ACADÊMICO')
    print('-----------------------------------------')
    print(f'MATÉRIA: {materia}.')
    print(f'NOTAS: A1 - {n1}, A2 - {n2}, A3 - {n3}.')
    print(f'FREQUÊNCIA: {freq}%.')
    print(f'RESULTADO: Média: {res:.1f} , Final: {apv}. ')

    dados_materia = {
        'nome': materia,
        'notas': [n1, n2, n3],
        'media': res,
        'frequencia': freq,
        'status': apv
    }
    historico_materias.append(dados_materia)

    pergunta = input('Deseja verificar mais notas? (S/n) ').lower()
    if pergunta != 's':
        break

gerar_relatorio(historico_materias)
