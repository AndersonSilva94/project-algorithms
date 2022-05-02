"""
Requisito 3: Passos a se seguir
1 - Criar um algoritmo que compare duas strings e identifique se uma
    é anagrama da outra
2 - Deve ser case insensitve

Lógica a se pensar:
1 - Verificar se as strings são vazias, caso contrário retornar False
2 - Criar uma função que vai converter cada string para lista e realizar
    o sorting, trazendo essa lista ordenada como retorno da função
3 - Utilizar bubble sort para fazer a ordenação
    - Algoritmo bubble sort consultado no link do conteúdo do course:
"""


def sorting(string):
    letter_list = list(string.lower())
    exchange = True
    counter_pass = 0
    while exchange:
        exchange = False
        for i in range(len(letter_list) - counter_pass - 1):
            if letter_list[i] > letter_list[i + 1]:
                letter_list[i], letter_list[i + 1] = \
                    letter_list[i + 1], letter_list[i]
                exchange = True
        counter_pass += 1
    return letter_list


def is_anagram(first_string, second_string):
    if first_string == '' or second_string == '':
        return False
    return sorting(first_string) == sorting(second_string)
