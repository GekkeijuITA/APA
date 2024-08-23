import random

dict = {
   "P": "Probabilmente primo",
   "C": "Probabilmente composto"
}

def MCPrimalityTest(n, a=None):
  s = 0
  q = n - 1
  while q % 2 == 0:
    s += 1
    q //= 2
  if a is None:
      a = random.randint(2,n-2)
  x = pow(a, q, n)
  if x == 1 or x == n-1:
    return dict["P"]
  while s-1 >= 0:
    x = pow(x, 2, n)
    if x == n-1:
      return dict["P"]
    s -= 1
  return dict["C"]

def MCD(a, b):
    while b:
        a, b = b, a % b
    return a

def Z(n):
  return [a for a in range(1,n) if MCD(a,n) == 1]

def H(n):
  return [a for a in Z(n) if pow(a,n-1,n) == 1]

def MRLiars(witnesses, n):
  L = []
  for a in witnesses:
    if MCPrimalityTest(n,a) == dict["P"]:
      L.append(a)
  return L

carmichael = [561,1105,1729,2465,2821,6601,8911]
for n in carmichael:
  primality = MCPrimalityTest(n)
  if primality == dict["C"]:
    Hn = H(n)
    liars = MRLiars(Hn, n)
    print(f"I bugiardi per {n}({len(liars)}) sono: {liars}")