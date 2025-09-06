import matplotlib.pyplot as plt
import math
import numpy as np

def f_exp(x, N):
    e_aprox = 0
    for n in range(N):
        e_aprox += (x**n)/math.factorial(n)
    return e_aprox

def f_sen(x, N):
    sen_aprox = 0
    for n in range(N):
        sinal = (-1)**n
        num = (x ** (2*n + 1))
        den = math.factorial(2*n + 1)
        sen_aprox = sen_aprox + (sinal * num)/den
    return sen_aprox

def f_cos(x, N):
    cos_aprox = 0
    for n in range(N):
        sinal = (-1)**n
        num = (x ** (2*n))
        den = math.factorial(2*n)
        cos_aprox = cos_aprox + (sinal * num)/den
    return cos_aprox

def show_graph(resultado, nome, cor):
    plt.figure(figsize = (10, 6))
    plt.plot(valores_continuos, resultado, label = nome, linewidth = 2, color = cor, linestyle = 'dashed')
    plt.legend(fontsize = 14)  
    plt.xlabel('Eixo x', fontsize = 16)
    plt.ylabel('Eixo y', fontsize = 16)
    plt.title(nome, fontsize = 20)
    plt.grid(True, linestyle = '-.', alpha = 0.7)
    plt.show()

def show_exp():
    resultado_exp = f_exp(valores_continuos, N)
    show_graph(resultado_exp, "Função Exponencial", "green")

def show_sen():
    resultado_sen = f_sen(valores_continuos, N)
    show_graph(resultado_sen, "Função Seno", "blue")

def show_cos():
    resultado_cos = f_cos(valores_continuos, N)
    show_graph(resultado_cos, "Função Cosseno", "red")

valores_continuos = np.linspace(-6, 6, 100)
N = 15

opcao = input("conta, calc_func, graficos, sair: ")
while opcao != "conta" and opcao != "calc_func" and opcao != "graficos" and opcao != "sair":
    opcao = input("conta, calc_func, graficos, sair: ")

while opcao != "sair":
    if opcao == "conta":
        operacao = input("Escolha uma das operacoes + - * / %: ")
        while operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/" and operacao != "%":
            operacao = input("Escolha uma das operacoes + - * / %: ")

        try:
            valor1 = float(input("Digite o valor 1: "))
            valor2 = float(input("Digite o valor 2: "))

            if operacao == "+":
                resultado = valor1 + valor2
                print(f"A soma entre {valor1} e {valor2} é {resultado}")

            elif operacao == "-":
                resultado = valor1 - valor2
                print(f"A subtracao entre {valor1} e {valor2} é {resultado}")

            elif operacao == "*":
                resultado = valor1 * valor2
                print(f"A multiplicacao entre {valor1} e {valor2} é {resultado}")
        
            elif operacao == "/":
                resultado = valor1 / valor2
                print(f"A divisao entre {valor1} e {valor2} é {resultado}")

            elif operacao == "%":
                resultado = valor1 % valor2
                print(f"O resto da divisao entre {valor1} e {valor2} é {resultado}")
            
        except ValueError:
            print("Digite numeros")
        
        except ZeroDivisionError:
            print("Nao existe divisao por zero")

    elif opcao == "calc_func":
        func = input("exp, sen, cos: ")
        while func != "exp" and func != "sen" and func != "cos":
            func = input("exp, sen, cos: ")

        valor = float(input("digite o valor: "))
        
        if func == "exp":
            resultado_exp = f_exp(valor, N)
            print(resultado_exp)

        elif func == "sen":
            resultado_sen = f_sen(valor, N)
            print(resultado_sen)
        
        elif func == "cos":
            resultado_cos = f_cos(valor, N)
            print(resultado_cos)
    
    elif opcao == "graficos":
        graficos = input("exp, sen, cos: ")
        while graficos != "exp" and graficos != "sen" and graficos != "cos":
            graficos = input("exp, sen, cos: ")

        if graficos == "exp":
            show_exp()

        elif graficos == "sen":
            show_sen()

        elif graficos == "cos":
            show_cos()
    
    
    opcao = input("conta, calc_func, graficos, sair: ")
    while(opcao != "conta" and opcao != "calc_func" and opcao != "graficos" and opcao != "sair"):
        opcao = input("conta, calc_func, graficos, sair: ")