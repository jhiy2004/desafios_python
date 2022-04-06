def fatorial(n, show=False):
    """
        -> Calcula o Fatorial de um número.
        :param n: O número a ser calculado.
        :param show: (opcional) Mostrar ou não a conta.
        :return: O valor do Fatorial de um número n.
    """
    res = 1
    res_string = ''
    for m in range(n, 0, -1):
        res = res * m
        if show:
            if m == 1:
                res_string += f'{m} = {res}'
                return res_string
            else:
                res_string += f'{m} x '
    return res

print(fatorial(7, show=True))