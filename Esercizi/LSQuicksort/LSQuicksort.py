import random
from tqdm import tqdm
import matplotlib.pyplot as plt
import math

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
    if (len(Sequence) <= 1):
        return Sequence
    pos = random.randint(0, len(Sequence)-1)
    s = Sequence[pos]
    confronto = confronta(s, pos, Sequence)
    sequenceMin = LVQuickSort(confronto[0])
    sequenceMax = LVQuickSort(confronto[1])
    sorted_sequence = sequenceMin
    sorted_sequence.extend([s])
    sorted_sequence.extend(sequenceMax)
    return sorted_sequence

def random_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, n))
    return arr

def valore_medio(R, Xr):
    sommatoria = sum(Xr)
    return (1/R) * sommatoria

def deviazione_standard(R, Xr, u):
    sommatoria = 0
    for i in Xr:
        sommatoria += ((i-u)**2)
    return (1/(R-1)) * sommatoria

def markov(mu, val):
    return mu/(val*mu)

def chebyshev(mu, val, dev):
    return dev / (((val-1)**2)*(mu**2))

def conta_frequenze(Xr, n):
    k = 0
    for x in Xr:
        if x >= n*val_medio:
            k += 1
    return k

n = 10**4
R = 10**5
Xr = []
array = random_array(n)

for i in tqdm(range(R)):
    X = 0
    LVQuickSort(array)
    Xr.append(X)

val_medio = valore_medio(R, Xr)
dev_standard = deviazione_standard(R, Xr, val_medio)

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

print(chebyshev(val_medio, v1, dev_standard))
print(chebyshev(val_medio, v2, dev_standard))

print("Frequenza empirica di X per il doppio: ", conta_frequenze(Xr, 2)/R)
print("Frequenza empirica di X per il triplo: ", conta_frequenze(Xr, 3)/R)