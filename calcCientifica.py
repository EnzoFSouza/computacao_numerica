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
    return math.floor(x)
    
def f_teto(x):
    return math.ceil(x)

def tratarTxt(txt):
    if "/" in txt:
        numero_txt = txt[txt.find("/") + 1:]
        numero = float(int(numero_txt))
        return np.pi / numero

    elif "*" in txt:
        numero_txt = txt[txt.find("*") + 1:]
        numero = float(int(numero_txt))
        return np.pi * numero
    
    else:
        return np.pi
    
def show_graph(resultado, pontos, nome, cor):
    plt.figure(figsize = (10, 6))
    plt.plot(valores_continuos, resultado, label = nome, linewidth = 2, color = cor)
    plt.legend(fontsize = 14)  
    plt.xlabel('Eixo x', fontsize = 16)
    plt.ylabel('Eixo y', fontsize = 16)
    plt.title(nome, fontsize = 20)
    plt.grid(True, linestyle = '-.', alpha = 0.7)
    plt.scatter(lista_valores_x_func, pontos)
    for i in range(len(lista_valores_x_func)):
        plt.annotate(
            f'({lista_valores_x_func[i]:.3f}, {pontos[i]:.3f})',
            xy = (lista_valores_x_func[i], pontos[i])
        )

    plt.show()

def show_exp():
    resultado_exp = f_exp(valores_continuos, N)
    pontos_exp = f_exp(lista_valores_x_func, N)
    show_graph(resultado_exp, pontos_exp, "Função Exponencial", "green")

def show_sen():
    resultado_sen = f_sen(valores_continuos, N)
    pontos_sen = f_sen(lista_valores_x_func, N)
    show_graph(resultado_sen, pontos_sen, "Função Seno", "blue")

def show_cos():
    resultado_cos = f_cos(valores_continuos, N)
    pontos_cos = f_cos(lista_valores_x_func, N)
    show_graph(resultado_cos, pontos_cos, "Função Cosseno", "red")

def show_tg():
    resultado_tg = f_tg(valores_continuos, N)
    pontos_tg = f_tg(lista_valores_x_func, N)
    show_graph(resultado_tg, pontos_tg, "Função Tangente", "green")

def show_sec():
    resultado_sec = f_sec(valores_continuos, N)
    pontos_sec = f_sec(lista_valores_x_func, N)
    show_graph(resultado_sec, pontos_sec, "Função Secante", "blue")

def show_cotg():
    resultado_cotg = f_cotg(valores_continuos, N)
    pontos_cotg = f_cotg(lista_valores_x_func, N)
    show_graph(resultado_cotg, pontos_cotg, "Função Cotangente", "blue")

def show_cossec():
    resultado_cossec = f_cossec(valores_continuos, N)
    pontos_cossec = f_cossec(lista_valores_x_func, N)
    show_graph(resultado_cossec, pontos_cossec, "Função Cossecante", "blue")

def show_senh():
    resultado_senh = f_senh(valores_continuos, N)
    pontos_senh = f_senh(lista_valores_x_func, N)
    show_graph(resultado_senh, pontos_senh, "Função Seno Hiperbólico", "yellow")

def show_cosh():
    resultado_cosh = f_cosh(valores_continuos, N)
    pontos_cosh = f_cosh(lista_valores_x_func, N)
    show_graph(resultado_cosh, pontos_cosh, "Função Cosseno Hiperbólico", "green")

def show_tgh():
    resultado_tgh = f_tgh(valores_continuos, N)
    pontos_tgh = f_tgh(lista_valores_x_func, N)
    show_graph(resultado_tgh, pontos_tgh, "Função Tangente Hiperbólica", "green")

lista_opcoes = ["conta", "calc_func", "graficos", "sair"]
lista_operacoes = ["+", "-", "*", "/", "%"]
lista_funcoes = ["abs", "piso", "teto", "exp", "sen", "cos", "tg", "sec", "cossec", "cotg", "senh", "cosh", "tgh"]
lista_valores_x_func = np.array([])
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

        valor = input("digite o valor: ")

        if "pi" in valor:
            valor = tratarTxt(valor)

        else:
            valor = float(valor)

        lista_valores_x_func = np.append(lista_valores_x_func, valor)

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
        graficos = input("exp, sen, cos, tg, sec, cossec, cotg, senh, cosh, tgh: ")
        while graficos not in lista_funcoes:
            graficos = input("exp, sen, cos, tg, sec, cossec, cotg, senh, cosh, tgh: ")

        if graficos == "exp":
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