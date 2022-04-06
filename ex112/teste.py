from utilidadesCeV import moeda
from utilidadesCeV import dado

preco = dado.leia_dinheiro('Digite o preco: R$')
moeda.resumo(preco, 20, 12)