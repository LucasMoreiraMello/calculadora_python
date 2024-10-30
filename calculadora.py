#!/bin/bash

nome = input('Digite o seu nome: ')
rodar_calculadora = input(f"{nome}, Deseja Iniciar a Calculadora? sim ou não:  ")
while rodar_calculadora == "sim":
    operador = input(f"{nome}, Selecione uma das seguintes operações: + , - , * , / : ---> ")
    if operador == '+' or operador == '-' or operador == '*' or operador == '/':
        num1 = int(input('Perfeito, agora digite o primeiro número: '))
        num2 = int(input('Agora digite o segundo número: '))
        if operador == '+':
            print(f"o valor é ---> {num1 + num2}")
        elif operador == '-':
            print(f"o valor é ---> {num1 - num2}")
        elif operador == '*':
            print(f"o valor é ---> {num1 * num2}")
        elif operador == '/':
            print(f"o valor é ---> {num1 / num2}")
        rodar_calculadora = input('Operação realizada com sucesso, quer realizar outra operação? sim ou não: ---> ')
        while rodar_calculadora != 'sim' and rodar_calculadora != 'não':
            rodar_calculadora = input('Digite um valor válido: ---> ')
        print('Foi um Prazer, volte sempre!')
            
    else:
        rodar_calculadora = input('Operador inválido, quer tentar digitar novamente? sim ou não: ---> ')
        while rodar_calculadora != 'sim' and rodar_calculadora != 'não':
            rodar_calculadora = input('Digite um valor válido: ---> ')
        if rodar_calculadora == 'não':
            print('Foi um Prazer, volte sempre!')
