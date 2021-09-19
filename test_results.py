import pytest

from sum_list import calculate_list, combinations

"""
Escreva uma função que recebe um array nao vazio de inteiros distintos e um inteiro representando uma soma alvo. 
Se quaisquer dois números no array de entrada somam a soma alvo, a função deve retornar-los no array de saida em 
qualquer ordem. Se nenhum par de numeros no array de entrada somarem a soma alvo, a função deve retornar a um 
array vazio. Note que a soma alvo deve ser obtida somando dois inteiros diferentes do array, você não pode somar 
um inteiro com ele mesmo.Você pode assumir que existira no maximo um par de números somando a soma alvo.

Exemplo de entrada
Array [3,5, -4, 8, 11, 1, -1, 6,]
TargetSum = 10

Exemplo de saida
[-1, 11] // pode ser na ordem invertida
"""


@pytest.mark.parametrize('numbers_list, soma_alvo, result', (
        ([], 8, []),
        ([1, 2], 4, []),
        ([1, 2, 3, 8, 7], 10, [[2, 8], [3, 7]]),
        ([1, 2, 3, 9], 5, [[2, 3]]),
        ([1, 3, 6, 14], 20, [[6, 14]]),
        ([1, 4, 1, -5, 12, -8, -2], 10, [[-2, 12]]),
))
def test_list_sum(numbers_list, soma_alvo, result):
    res = calculate_list(numbers_list, soma_alvo)
    assert res == result


@pytest.mark.parametrize('numbers_list, soma_alvo, result', (
        ([], 8, []),
        ([1, 2], 4, []),
        ([1, 2, 3, 8, 7], 10, [[2, 8], [3, 7]]),
        ([1, 2, 3, 9], 5, [[2, 3]]),
        ([1, 3, 6, 14], 20, [[6, 14]]),
        ([1, 4, 1, -5, 12, -8, -2], 10, [[-2, 12]]),
))
def test_combinations(numbers_list, soma_alvo, result):
    res = combinations(numbers_list, soma_alvo)
    assert res == result