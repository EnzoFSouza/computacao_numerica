import matplotlib.pyplot as plt
import math
import numpy as np

def f_abs(x):
    return abs(x)

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

def f_tg(x, N):
    tg_aprox = f_sen(x, N) / f_cos(x, N)
    return tg_aprox

def f_sec(x, N):
    sec_aprox = 1 / f_cos(x, N)
    return sec_aprox

def f_cossec(x, N):
    cossec_aprox = 1 / f_sen(x, N)
    return cossec_aprox

def f_cotg(x, N):
    cotg_aprox = 1 / f_tg(x, N)
    return cotg_aprox

def f_senh(x, N):
    senh_aprox = 0
    for n in range(N):
        num = (x ** (2*n + 1))
        den = math.factorial(2*n + 1)
        senh_aprox = senh_aprox + (num/den)
    return senh_aprox

def f_cosh(x, N):
    cosh_aprox = 0
    for n in range(N):
        num = (x ** (2*n))
        den = math.factorial(2*n)
        cosh_aprox = cosh_aprox + (num/den)
    return cosh_aprox

def f_tgh(x, N):
    tgh_aprox = f_senh(x, N) / f_cosh(x, N)
    return tgh_aprox

def f_piso(x):
    if x >= 0:
        return int(x)
    
    else:
        if x == int(x):
            return int(x)

        else:
            return int(x) - 1

def f_teto(x):
    if x == int(x):
        return int(x)

    elif x > 0:
        return int(x) + 1

    else:
        return int(x)

def show_graph(resultado, nome, cor):
    plt.figure(figsize = (10, 6))
    plt.plot(valores_continuos, resultado, label = nome, linewidth = 2, color = cor)
    plt.legend(fontsize = 14)  
    plt.xlabel('Eixo x', fontsize = 16)
    plt.ylabel('Eixo y', fontsize = 16)
    plt.title(nome, fontsize = 20)
    plt.grid(True, linestyle = '-.', alpha = 0.7)
    plt.show()

def show_abs():
    resultado_abs = f_abs(valores_continuos)
    show_graph(resultado_abs, "Função Módulo", "red")

"""def show_piso():
    resultado_piso = f_piso(valores_continuos)
    show_graph(resultado_piso, "Função Piso", "red")

def show_teto():
    resultado_teto = f_teto(valores_continuos)
    show_graph(resultado_teto, "Função Teto", "red")
"""
def show_exp():
    resultado_exp = f_exp(valores_continuos, N)
    show_graph(resultado_exp, "Função Exponencial", "green")

def show_sen():
    resultado_sen = f_sen(valores_continuos, N)
    show_graph(resultado_sen, "Função Seno", "blue")

def show_cos():
    resultado_cos = f_cos(valores_continuos, N)
    show_graph(resultado_cos, "Função Cosseno", "red")

def show_tg():
    resultado_tg = f_tg(valores_continuos, N)
    show_graph(resultado_tg, "Função Tangente", "green")

def show_sec():
    resultado_sec = f_sec(valores_continuos, N)
    show_graph(resultado_sec, "Função Secante", "blue")

def show_cotg():
    resultado_cotg = f_cotg(valores_continuos, N)
    show_graph(resultado_cotg, "Função Cotangente", "blue")

def show_cossec():
    resultado_cossec = f_cossec(valores_continuos, N)
    show_graph(resultado_cossec, "Função Cossecante", "blue")

def show_senh():
    resultado_senh = f_senh(valores_continuos, N)
    show_graph(resultado_senh, "Função Seno Hiperbólico", "yellow")

def show_cosh():
    resultado_cosh = f_cosh(valores_continuos, N)
    show_graph(resultado_cosh, "Função Cosseno Hiperbólico", "green")

def show_tgh():
    resultado_tgh = f_tgh(valores_continuos, N)
    show_graph(resultado_tgh, "Função Tangente Hiperbólica", "green")

lista_opcoes = ["conta", "calc_func", "graficos", "sair"]
lista_operacoes = ["+", "-", "*", "/", "%"]
lista_funcoes = ["abs", "piso", "teto", "exp", "sen", "cos", "tg", "sec", "cossec", "cotg", "senh", "cosh", "tgh"]
valores_continuos = np.linspace(-6, 6, 100)
N = 15

opcao = input("conta, calc_func, graficos, sair: ")
while opcao not in lista_opcoes:
    opcao = input("conta, calc_func, graficos, sair: ")

while opcao != "sair":
    if opcao == "conta":
        operacao = input("Escolha uma das operacoes + - * / %: ")
        while operacao not in lista_operacoes:
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
        func = input("abs, piso, teto, exp, sen, cos, tg, sec, cossec, cotg, senh, cosh, tgh: ")
        while func not in lista_funcoes:
            func = input("abs, piso, teto, exp, sen, cos, tg, sec, cossec, cotg, senh, cosh, tgh: ")

        valor = float(input("digite o valor: "))
        
        if func == "abs":
            resultado_abs = f_abs(valor)
            print(resultado_abs)

        elif func == "piso":
            resultado_piso = f_piso(valor)
            print(resultado_piso)
        
        elif func == "teto":
            resultado_teto = f_teto(valor)
            print(resultado_teto)

        elif func == "exp":
            resultado_exp = f_exp(valor, N)
            print(resultado_exp)

        elif func == "sen":
            resultado_sen = f_sen(valor, N)
            print(resultado_sen)
        
        elif func == "cos":
            resultado_cos = f_cos(valor, N)
            print(resultado_cos)
        
        elif func == "sec":
            resultado_sec = f_sec(valor, N)
            print(resultado_sec)

        elif func == "cossec":
            resultado_cossec = f_cossec(valor, N)
            print(resultado_cossec)
        
        elif func == "cotg":
            resultado_cotg = f_cotg(valor, N)
            print(resultado_cotg)

        elif func == "tg":
            resultado_tg = f_tg(valor, N)
            print(resultado_tg)

        elif func == "senh":
            resultado_senh = f_senh(valor, N)
            print(resultado_senh)
        
        elif func == "cosh":
            resultado_cosh = f_cosh(valor, N)
            print(resultado_cosh)

        elif func == "tgh":
            resultado_tgh = f_tgh(valor, N)
            print(resultado_tgh)

    elif opcao == "graficos":
        graficos = input("abs, exp, sen, cos, tg, sec, cossec, cotg, senh, cosh, tgh: ")
        while graficos not in lista_funcoes:
            graficos = input("abs, exp, sen, cos, tg, sec, cossec, cotg, senh, cosh, tgh: ")

        if graficos == "abs":
            show_abs()

        #elif graficos == "piso":
        #    show_piso()
        
        #elif graficos == "teto":
        #    show_teto()

        elif graficos == "exp":
            show_exp()

        elif graficos == "sen":
            show_sen()

        elif graficos == "cos":
            show_cos()
        
        elif graficos == "tg":
            show_tg()

        elif graficos == "sec":
            show_sec()
        
        elif graficos == "cossec":
            show_cossec()
        
        elif graficos == "cotg":
            show_cotg()

        elif graficos == "senh":
            show_senh()

        elif graficos == "cosh":
            show_cosh()

        elif graficos == "tgh":
            show_tgh()

    opcao = input("conta, calc_func, graficos, sair: ")
    while opcao not in lista_opcoes:
        opcao = input("conta, calc_func, graficos, sair: ")