#Um prograam que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
n1 = float(input('Valor do produto: '))

desconto = (n1 * 5) / 100
preco = n1 - desconto

# preco = n1 - (n1 * 5 / 100)

print('O valor do produto com 5 % de desconto é: {:.2f} '.format(preco))