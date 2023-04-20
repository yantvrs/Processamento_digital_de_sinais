import numpy as np
import matplotlib.pyplot as plt

# Função que faz a estimativa da TFTD
def dtft(x, n, k):
    M = 150
    X = np.zeros_like(k,dtype=np.complex128)
    for i, freq in enumerate(k):
        X[i] = np.sum(x*np.exp(-1j*(np.pi/M)*n*freq))
    return X

n = np.arange(0,10)
x = (0.9*np.exp(1j*np.pi/3))**n
k = np.arange(-400,401)
X = dtft(x,n,k)

# Plota a magnetude de X(e^(jw))
plt.subplot(2,1,1)
plt.plot(k, np.abs(X))
plt.title('Magnitude X(e^(jw))')
plt.xlabel('Frequência (k)')
plt.ylabel('|X(e^(jw))|')
plt.grid(True)

# Plota a fase de X(e^(jw))
plt.subplot(2,1,2)
plt.plot(k, np.angle(X))
plt.title('Fase de X(e^(jw))')
plt.xlabel('Frequência (k)')
plt.ylabel('Ângulo X(e^(jw))(rad)')
plt.grid(True)

plt.tight_layout()
plt.show()
