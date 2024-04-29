texto = input("Informe um texto: ")
VOGAIS = "AEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛ"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


