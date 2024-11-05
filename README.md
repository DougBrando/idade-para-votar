# Verificação de Situação do Voto

Este programa em Python determina a situação do voto de um usuário com base em seu ano de nascimento. O programa considera as regras de elegibilidade para o voto no Brasil:

- **Menores de 16 anos**: Não podem votar (Status: Negado)
- **Idade entre 16 e 17 anos**: Voto opcional (Status: Opcional)
- **Idade entre 18 e 65 anos**: Voto obrigatório (Status: Obrigatório)
- **Acima de 65 anos**: Voto opcional (Status: Opcional)

## Funcionalidades

- Solicita ao usuário que insira seu ano de nascimento.
- Valida a entrada para garantir que:
  - O ano não seja no futuro.
  - O ano seja um número inteiro e razoável (maior que 1900).
- Calcula a idade com base no ano atual.
- Retorna uma mensagem informativa sobre a idade do usuário e sua situação de voto.

## Exemplo de Uso
```bash
Digite sua data de nascimento (AAAA): 1990
Sua idade é 34 e seu voto é Obrigatório.
