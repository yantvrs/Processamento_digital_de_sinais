import numpy as np
import matplotlib.pyplot as plt


# Estima a TFTD
def dtft(x,n,k):    
    M=len(k)  # Amostras
    X=np.zeros((1,M),dtype=np.complex128)
    # Somatório
    for i in range(M):
        X[0,i]=np.sum(x*np.exp(-1j*np.pi/M*np.outer(n.T,k[i])))
    return X

# Definindo a sequência x[n] = (0,9*exp(jπ/3))^n, 0 ≤ n ≤ 10
n = np.arange(11)
x = (0.9*np.exp(1j*np.pi/3))**n

# Calculando TFTD
k = np.arange(501)
X = dtft(x,n,k)

# Plota a magnitude de X(e^(jw))
plt.subplot(2,1,1)
plt.plot(k,np.abs(X[0,:]))
plt.title('Magnitude X(e^(jw))')
plt.xlabel('Frequência (k)')
plt.ylabel('|X(e^(jw))|')
plt.grid(True)

# Plota a fase de X(e^(jw))
plt.subplot(2,1,2)
plt.plot(k,np.angle(X[0,:]))
plt.title('Fase de X(e^(jw))')
plt.xlabel('Frequência (k)')
plt.ylabel('Ângulo X(e^(jw))(rad)')
plt.grid(True)

plt.tight_layout()
plt.show()
