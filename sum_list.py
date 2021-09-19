import itertools


def calculate_list(numbers_list=None, soma_alvo=10):
    """
    Usei coisa básicas, acho que existem soluções bem melhores, especialmente em functools
    """
    if numbers_list is None:  # apesar de o enunciado afirmar que a lista não é vazia, eu a testo
        numbers_list = []

    """assumimos que numbers_list é uma lista de inteiros - aqui eu não validei"""
    results = []  # uma lista de resultados, para evitar diplicidades (assim entendi no enunciado)
    if len(numbers_list) <= 1:  # se a lista não tiver um par de inteiros, retorna vazia
        return results

    # Detesto usar for encadeados, acho sempre que existe uma solução melhor. Mas preferi ficar o básico mesmo
    for i in range(len(numbers_list)-1):  #itera a lista, com exceção do últio elemento
        for j in range(len(numbers_list)):  # itera a lista toda (aqui está o encadeamento que não gostei
            if i == j:  # o enunciado proíbe somar números iguais, então ignoramo-os
                continue
            cur_list = [numbers_list[i], numbers_list[j]]  # a lista corrente, que terá os dois valores oriundos dos dois for, já citados antes

            # uma vez que a ordem dos fatores é intiferente, optei por ordená-las, antes de fazer o teste de se já estão
            # presentes no resultado final e se a soma é igual à soma-alvo.
            # Cada par estará numa lista que será anexada a uma lista de resultados
            # Obs: ignorei a premissa de que haverá apenas uma dupla que terá a soma alvo, já que eu evitei a duplicitade.
            if sorted(cur_list) not in results and sum(cur_list) == soma_alvo:
                cur_list = sorted(cur_list)
                results.append(cur_list)

    return results


def combinations(numbers_list=None, soma_alvo=10):
    results = []
    combined = itertools.combinations(numbers_list, 2)
    my_list = [c for c in combined]
    for tup in my_list:
        if tup[0] == tup[1]:
            continue
        if sum(tup) == soma_alvo and list(tup) not in results:
            results.append(sorted(tup))
    return results