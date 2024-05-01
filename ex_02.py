# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 km/litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obet a distância percorrida com a fórmula DISTANCIA = TEMPO*VELOCIDADE. Tendo o valor da distência, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA/12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

tem = float(input('Qual foi o tempo gasto da viagem [horas]: '))
vel = float(input('Qual foi a velocidade média da viagem [km]: '))

val = float(input('Qual é o preço da gasolina: '))
dis = round(vel*tem, 2)

lit = round(dis / 12,2)

gas = round(val*lit, 2)

print(f'Nesta viagem foi de {dis} km e foi gasto {gas} R$ de gasolina')