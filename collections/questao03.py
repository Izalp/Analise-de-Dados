def obter_dados():
    while True:
        try:
            aluno = input('Insira o nome do aluno: ').strip()
            if not aluno:
                raise ValueError('O nome do aluno não pode estar vazio.')
            media = float(input('Insira a média do aluno (0 a 100): '))
            if media < 0 or media > 100:
                raise ValueError('A média deve estar entre 0 e 100.')
            return aluno, media
        except ValueError as e:
            print(f'Entrada inválida: {e}. Tente novamente.')

def verificar_media(nome, media):
    status = 'aprovado' if media >= 60 else 'reprovado'
    return {
        'nome': nome,
        'media': media,
        'status': status
    }
    
aluno, media = obter_dados()
dados_aluno = verificar_media(aluno, media)

print(f'\n{dados_aluno["nome"]} foi {dados_aluno["status"]} com a média de {dados_aluno["media"]:.1f}.')
print(f'Dicionário: {dados_aluno}')