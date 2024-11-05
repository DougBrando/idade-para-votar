from datetime import datetime

def vota(ano_nascimento):
    """
    Calcula a situação do voto com base na idade do usuário.

    Parâmetros:
    ano_nascimento (int): O ano de nascimento do usuário.

    Retorna:
    str: Mensagem informando a idade e a situação do voto.
    """
    # Obtém o ano atual
    ano_atual = datetime.now().year
    
    # Calcula a idade
    idade = ano_atual - ano_nascimento
    
    # Verifica a situação do voto com base na idade
    if idade < 16:
        status_voto = 'Negado'  # Não pode votar
    elif 16 <= idade < 18 or idade > 65:
        status_voto = 'Opcional'  # Voto opcional
    else: 
        status_voto = 'Obrigatório'  # Voto obrigatório
    
    # Retorna a mensagem com a idade e a situação do voto
    return f'Sua idade é {idade} e seu voto é {status_voto}.'

def obter_ano_nascimento():
    """
    Solicita ao usuário que insira seu ano de nascimento e valida a entrada.

    Retorna:
    int: O ano de nascimento do usuário.
    """
    while True:
        try:
            ano_nascimento = int(input('Digite sua data de nascimento (AAAA): '))
            # Verifica se o ano de nascimento é razoável
            if ano_nascimento > datetime.now().year:
                print("A data de nascimento não pode ser no futuro. Tente novamente.")
            elif ano_nascimento < 1900:  # Supondo que ninguém nasceu antes de 1900
                print("Por favor, insira um ano válido (maior que 1900).")
            else:
                return ano_nascimento
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def main():
    """Função principal que executa o programa."""
    ano_nascimento = obter_ano_nascimento()  # Obtém o ano de nascimento do usuário
    resultado = vota(ano_nascimento)  # Calcula a situação do voto
    print(resultado)  # Imprime o resultado

if __name__ == "__main__":
    main()  # Executa a função principal
