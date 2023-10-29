# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

num = int(input("Digite um número de 3 dígitos: "))
centena = num//100
dez = (num%100)//10
unidade = num%10

print(f"O valor invertido é {unidade}{dez}{centena}")

# num: armazena o número digitado pelo usuário.
# centena: armazena o valor da centena do número digitado pelo usuário. Para isso, ele divide por 100 e obtêm o quociente da divisão.
# dez: armazena o valor da dez do número digitado. Ele obtêm o resto da divisão do número por 100. Em seguida, divide o resto por 10 e obtêm o quociente da divisão.
# unidade: armazena o valor da unidade do número digitado. Ele obtêm o resto da divisão por 10.
