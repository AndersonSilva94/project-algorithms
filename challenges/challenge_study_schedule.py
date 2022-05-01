"""
Requisito 1 - Passos a se seguir:
1 - Descobrir o maior horário com pessoas acessando a plataforma
2 - Para isso usar as seguintes informações:
2.1 - A função irá receber uma lista de tuplas onde cada tupla
    registra o horário de entrada e saída de cada estudante
2.2 - A função também irá receber uma variável que vai ser chamada
    várias vezes com valores diferentes
3 - Algoritmo deve usar solução iterativa
4 - Caso o target_time passado seja nulo, o valor retornado deve ser None
    Ex: 0 é um valor nulo
5 - Se permanece_period receber uma entrada inválida retornar None
6 - Retornar a quantidade de estudantes presentes para uma entrada específica

Lógica a se seguir:
1 - Verificar se target_time é nulo
2 - Percorrer a lista e verificar se os valores de entrada e saída são nulos
3 - Criar uma variável que vai somar + 1 sempre que determinado valor condizer
    com o tempo de entrada - saída
"""


def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    students = 0
    for start_period, end_period in permanence_period:
        "istanceof é um método que verifica se a variável possui o tipo"
        if not isinstance(start_period, int) \
                or not isinstance(end_period, int):
            return None
        if start_period <= target_time <= end_period:
            students += 1
    return students
