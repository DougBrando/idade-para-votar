def vota(ano_nascimento):
    # Calcula a idade com base no ano atual (2024)
    idade = 2024 - ano_nascimento

    # Verifica a situação do voto com base na idade
    if idade < 16:
        status_voto = 'Negado'  # Não pode votar
    elif 16 <= idade < 18 or idade > 65:
        status_voto = 'Opcional'  # Voto opcional
    else:
        status_voto = 'Obrigatório'  # Voto obrigatório

    # Retorna a mensagem com a idade e a situação do voto
    return f'Sua idade é {idade} e seu voto é {status_voto}.'


# Solicita ao usuário que digite o ano de nascimento
ano_nascimento = int(input('Digite sua data de nascimento (AAAA): '))

# Chama a função vota e imprime o resultado
print(vota(ano_nascimento))
