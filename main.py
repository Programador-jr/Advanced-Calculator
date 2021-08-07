from colorama import Fore
from time import sleep
from os import system

print(
    "*NOTA* Ao criar uma raiz cúbica de 64, você obterá 3,99999999999999996.  Embora isso também seja correto, arredonde para cima e use 4. Além disso, os resultados das últimas quatro operações podem ser uma casa decimal longa. É preferível. \n \n "
)
print(Fore.LIGHTYELLOW_EX + "Download do software" + Fore.LIGHTBLUE_EX +
      "O sistema está acordando")
sleep(2)
dddddd = 1
while dddddd < 100:

	print(
	    Fore.BLUE +
	    " \n\n 1. adição \n 2. subtração \n 3. multiplicação \n 4. divisão \n 5. quadrado \n 6. raiz quadrada \n 7. cubo \n 8. raiz cúbica \n 9. diâmetro e raio \n 10. circunferência  \n 11.área e retângulos de perímetro \n 12.área de círculos \n 13.Área de triângulos \n 14. Área de trapézios \n 15.módulo \n 16. exponentes \n 17. Volume de esferas \n 18. Volume de prismas triangulares \n 19. Volume de prismas trapazoidais \n 20. Volume de prismas retangulares \n 21. Celcius para Farenheit \n 22.Farenheight to celcius \n 23.Pés para metros \n 24. Metros para pés \n  "
	)
	opt = input(Fore.GREEN + "\nEscolha um número da" + Fore.YELLOW +
	            "lista" + Fore.GREEN + ": " + Fore.LIGHTMAGENTA_EX)
	if (opt == str):
		print("Ei, isso não é um número!")
	elif (opt == "1") or (opt == "1."):
		num1 = float(input(Fore.LIGHTGREEN_EX + "\nEscolha o seu primeiro número: "))
		num2 = float(input(Fore.LIGHTBLUE_EX +
		                   "\nEscolha o seu segundo número: "))
		print(Fore.YELLOW + "\n", num1 + num2)


	elif (opt == "2") or (opt == "2."):
		num3 = float(input(Fore.LIGHTGREEN_EX +
		                   "\nSelecione seu primeiro número: "))
		num4 = float(input(Fore.LIGHTBLUE_EX +
		                   "\nSelecione seu segundo número: "))
		print(Fore.YELLOW + "\n", num3 - num4)
  

	elif (opt == "3") or (opt == "3."):
		num5 = float(input(Fore.LIGHTGREEN_EX + "\nEscolha um multiplicando: "))
		num6 = float(input(Fore.LIGHTBLUE_EX + "\nEscolha um multiplicador: "))
		print(Fore.YELLOW + "\n", num5 * num6)

	elif (opt == "4") or (opt == "4."):
		num7 = float(input(Fore.LIGHTGREEN_EX + "\nEscolha o dividendo: "))
		num8 = float(input(Fore.LIGHTBLUE_EX + "\nEscolha o divisor: "))
		quote = (num7 / num8)
		print(Fore.YELLOW + "\n", quote)

	elif (opt == "5") or (opt == "5."):
		num9 = float(input(Fore.LIGHTGREEN_EX + "\nSelecione um número: "))
		sq = num9 * num9
		print(Fore.YELLOW + "\nSeu número ao quadrado é", sq)

	elif (opt == "6") or (opt == "6."):
		num10 = float(input(Fore.LIGHTGREEN_EX + "\nInsira um número: "))
		sqrt = num10**0.5
		print(Fore.YELLOW + "\nA raiz quadrada do seu número é", sqrt)

	elif (opt == "7") or (opt == "7."):
		num11 = float(input(Fore.LIGHTGREEN_EX + "\nInsira um número: "))
		cb = num11**3
		print(Fore.YELLOW + "\nSeu número ao cubo é", cb)

	elif (opt == "8") or (opt == "8."):
		num12 = float(input(Fore.LIGHTGREEN_EX + "\nEscolha um número: "))
		cbrt = num12**0.33333333333333334
		print(Fore.YELLOW + "\nA raiz cúbica do seu número é", cbrt)

	elif (opt == "9") or (opt == "9."):
		c = float(input(Fore.LIGHTGREEN_EX + "\nInsira a circunferência: "))
		d = c / 3.1415926535
		r = c / 6.283185307
		print(Fore.YELLOW + "\nSeu diâmetro é: ", d)
		print(Fore.YELLOW + "\nSeu raio é:", r)

	elif (opt == "10") or (opt == "10."):
		r2 = float(input(Fore.LIGHTGREEN_EX + "\nInsira seu raio: "))
		circfind = r2 * 6.283185307
		print(Fore.YELLOW + "\nA circunferência é ", circfind)

	elif (opt == "11") or (opt == "11."):
		arsq = float(input(Fore.LIGHTGREEN_EX + "\nQual é o comprimento? "))
		arsq2 = float(input(Fore.LIGHTBLUE_EX + "\nQual é a largura? "))
		mathfind = arsq * arsq2
		perm = arsq * 2
		perm2 = arsq2 * 2
		permfind = perm + perm2
		print(Fore.YELLOW + "\nA área é", mathfind)
		print(Fore.YELLOW + "\nO perímetro é", permfind)

	elif (opt == "12") or (opt == "12."):
		circar = float(input(Fore.LIGHTGREEN_EX + "\nQual é o raio? "))
		step1 = circar**2
		step2 = step1 * 3.1415926535
		print(Fore.YELLOW + "\nA área do círculo é", step2)

	elif (opt == "13") or (opt == "13."):
		tng1 = float(input(Fore.LIGHTGREEN_EX + "\nInsira a base: "))
		tng2 = float(input(Fore.LIGHTBLUE_EX + "\nInsira a altura: "))
		sap1 = tng1 * tng2
		sap2 = sap1 / 2
		print(Fore.YELLOW + "\nA área do triângulo é", sap2)

	elif (opt == "14") or (opt == "14."):
		trapb1 = float(
		    input(Fore.LIGHTGREEN_EX +
		          "\nQual é o comprimento da primeira base? "))
		trapb2 = float(
		    input(Fore.LIGHTBLUE_EX +
		          "\nQual é o comprimento da segunda base?"))
		traph1 = float(input(Fore.LIGHTRED_EX + "\nQual é a altura? "))
		findtrap1 = (trapb1 + trapb2) / 2
		findtrap2 = findtrap1 * traph1
		print(Fore.YELLOW + "\nA área é", findtrap2)

	elif (opt == "15") or (opt == "15."):
		mod1 = float(input(Fore.LIGHTGREEN_EX + "\nSelecione o dividendo: "))
		mod2 = float(input(Fore.LIGHTBLUE_EX + "\nSelecione o divisor: "))
		modulusend = mod1 % mod2
		print(Fore.YELLOW + "\n O módulo é", modulusend)
