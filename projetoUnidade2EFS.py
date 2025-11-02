#y = f[y(n - 2), y(n - 1), u(n), u(n - 1)]
#escolher centros
#definir s2
#construir matriz phi
#resolver sistema de equações lineares w = phi+ @ y
#regressao linear
#correlacao
#plotar dados


#importando
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
from numpy.linalg import pinv

#carregando dados
data = np.loadtxt('dados.txt', delimiter=',', skiprows=1)

#organizando em matrizes
t = data[:, 0] #tempo
u = data[:, 1] #entrada
x = data[:, 2] #saida
y = data[:, 3] #saida
x1 = data[:, 4]
y1 = data[:, 5]

#print(t.shape)
#print(u.shape)
#print(x.shape)
#print(y.shape)
#print(x1.shape)
#print(y1.shape)

#t = data[:, 0]
#u = data[:, 1]
#x = data[:, 2]
#y = data[:, 3]
#x1 = data[:, 4]
#y1 = data[:, 5]


#X = np.column_stack((t, u, x, y))
#X = np.column_stack((np.ones((X.shape[0], 1)), X))

#w = (la.inv(X.T@X))@X.T@y
#y_pred = X@w

#criando gaussianas
#baseando em t, pois u, x, y, x1 e y1 dependem de t
c = np.linspace(t[0], t[-1], 100)
s2 = 1

phi = np.exp(-((t[:, None] - c[None, :]) ** 2) / (2 * s2 * 2))
#print(phi)

w1 = la.pinv(phi) @ y
w2 = la.pinv(phi) @ x

y_est = phi @ w1
x_est = phi @ w2

EMQx = np.mean((x - x_est) ** 2)
EMQy = np.mean((y - y_est) ** 2)

print(EMQx)
print(EMQy)
plt.figure(figsize=(10, 7))
plt.subplot(3, 1, 1)
plt.plot(t, u, label='$u(t)$', color='k')
plt.ylabel('Sinal de Entrada : $u(t)$')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, x1, '--k', lw = 2.5, label='$x(t)$ original')
plt.plot(t, x, 'o', alpha = 0.2, label='$x(t)$ com ruido')
plt.plot(t, x_est, 'r--', label = "x1_est")
plt.ylabel('Saída 01 : $x(t)$')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, y1, '--k', lw = 2.5, label='$y(t)$ original')
plt.plot(t, y, 'og', alpha=0.2, label='$y(t)$ com ruido')
plt.plot(t, y_est, 'r--', label = "y1_est")
plt.xlabel('Tempo (s)')
plt.ylabel('Saída 02 : $y(t)$')
plt.legend()

plt.suptitle('Sistema Dinâmico a ser Identificado')
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
#plt.plot(t, y1_est, label = "y1_est")
#plt.plot(t, x1_est, label = "x1_est")
#plt.xlabel("x")
#plt.ylabel("y")
#plt.legend()
#plt.show()

"""
#baseando em u
c = np.linspace(u[0], u[-1], 4)
s2 = 1

phi = np.exp(-((u[:, None] - c[None, :]) ** 2) / (2 * s2 * 2))
#print(phi)

w = la.pinv(phi) @ y

y_est = phi @ w

plt.plot(u, y_est, label="y_est")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()"""