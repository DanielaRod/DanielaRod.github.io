print('Bem-vindo ao nosso programa!')
print('Este programa consiste em calcular o IMC de uma pessoa conforme o peso e altura.')
print('Caso queira sair do programa digite x')
print('Vamos começar!')


print ('Digite o seu peso em kg: ')
peso_kg = float(input())
print ('Digite o seu peso em cm: ')
altura_cm = float(input())
IMC = peso_kg / (altura_cm * altura_cm)
if IMC <= 18.5:
    print ('O teu IMC é ', IMC, 'o que significa que te encontras abaixo do peso')
elif IMC > 18.5 and IMC <= 25:
    print ('O teu IMC é', IMC, 'o que significa que te encontras no peso normal')
elif IMC > 25 and IMC < 30:
    print ('O teu IMC é', IMC, 'o que significa que te encontras acima do peso')
elif IMC >= 30:
    print ('O teu IMC é', IMC, 'o que significa que te encontras obeso')
  
