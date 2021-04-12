pesos = input(" ¿Cuántos cordobas nicaraguenses tenés?: ")
pesos = float (pesos)
valor_dolar = 35.50
valor_dolar = round (valor_dolar, 2)
dolares = pesos / valor_dolar
dolares = round (dolares, 2)
dolares = str (dolares)
print ("Tienes $" + dolares + " dolares")

dolares = input(" ¿Cuántos dolares nicaraguenses tenés?: ")
dolares = float (dolares)
valor_cordoba = 35.50
valor_cordoba = round (valor_cordoba, 2)
dolares = dolares * valor_cordoba
dolares = round (dolares, 2)
dolares = str (dolares)
print ("Tienes C$" + dolares + " cordobas ")