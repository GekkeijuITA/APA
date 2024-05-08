import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import math
import numpy as np

X = 0

def confronta(s, pos, Sequence):
    global X
    sequenceMin = []
    sequenceMax = []
    for i in range(len(Sequence)):
        if (i != pos):
            if Sequence[i] < s:
                sequenceMin.append(Sequence[i])
                X += 1
            else:
                sequenceMax.append(Sequence[i])
                X += 1
    return [sequenceMin, sequenceMax]

def LVQuickSort(Sequence):
    if (len(Sequence) <= 1): return Sequence
    pos = random.randint(0, len(Sequence)-1)
    s = Sequence[pos]
    confronto = confronta(s, pos, Sequence)
    sequenceMin = LVQuickSort(confronto[0])
    sequenceMax = LVQuickSort(confronto[1])
    return np.concatenate([sequenceMin, [s], sequenceMax])

def valore_medio(R, Xr):
    sommatoria = sum(Xr)
    return (1/R) * sommatoria

def varianza(R, Xr, u):
    sommatoria = 0
    for i in Xr:
        sommatoria += ((i-u)**2)
    return (1/(R-1)) * sommatoria

def markov(mu, k):
    return mu/(k*mu)

def chebyshev(mu, k, varianza):
    return varianza / (((k-1)**2)*(mu**2))

def conta_frequenze(Xr, n, val_medio):
    k = 0
    for x in Xr:
        if x >= n*val_medio:
            k += 1
    return k

n = 10**4
R = 10**5
Xr = []
array = np.random.randint(0, n, size=n)

for i in tqdm(range(R)):
    X = 0
    LVQuickSort(array)
    Xr.append(X)

val_medio = valore_medio(R, Xr)
varianza = varianza(R, Xr, val_medio)
dev_standard = math.sqrt(varianza)

print("Valore medio: ", val_medio)
print("Varianza: ", dev_standard)
print("Deviazione standard: ", math.sqrt(dev_standard))

plt.hist(Xr, edgecolor="black", bins=50)
plt.xlabel("Numero di confronti")
plt.ylabel("Frequenza")
plt.show()

v1 = 2
v2 = 3

print(markov(val_medio, v1))
print(markov(val_medio, v2))

print(chebyshev(val_medio, v1, varianza))
print(chebyshev(val_medio, v2, varianza))

print("Frequenza empirica di X per il doppio: ", conta_frequenze(Xr, v1, val_medio)/R)
print("Frequenza empirica di X per il triplo: ", conta_frequenze(Xr, v2, val_medio)/R)