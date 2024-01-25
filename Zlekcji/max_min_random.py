import random
random.seed(2)
tab = []
for i in range(10):
  a = int(input("podaj liczbę "))
  for j in range(2, a//2+1):
    if a %j ==0:
      break

#tablica liczb losowy 10 elementów losujemy od 1 do 100
# a = random.randint(1,100)
# tab = []
# a = int(input("podaj liczbę"))
# for i in range(a):
#   tab.append(input("Podaj ulubiony owoce  "))
# print(tab)


# a = int(input("podaj liczbę"))
# tab = [""]*a
# for i in range(a):
#   tab[i] = input("Podaj owoc")
# print(tab)

# a = int(input("podaj liczbę ocen\n"))
# tab = [0]*a
# for i in range(a):
#   tab[i] = int(input("Podaj ocenę"))
# print(tab)

tab = []
for i in range(10):
  tab.append(random.randint(1,100))
# print(tab)
# # print(tab[5])
min = tab[0]

for index in range(len(tab)): #index 0,1, 2
  if min > tab[index]:
    min = tab[index] 
# print(min)


dlugosc = 0
for i in tab: #i będzie wartością 
  dlugosc += 1
  if min > i:
    min = i
    # length
# print(dlugosc, len(tab))

a = int(input("podaj liczbę ocen\n"))
tab = []
for i in range(a):
  tab.append(int(input("podaj ocenę ")))
print(tab)
suma = 0
for i in tab:
  suma += i
print(suma/a) #suma/len(tab)

# szukamy max elementu w tablicy
# w tablicy zapisujemy dzielniki liczby podanej przez użytkownika 12 = 1 2 3 4 6 12
# 4 24 - nwd 
for i in range(10,1,-1):
  print(i)

a = random.randint(1,200) #losuje
a = int(input("podaj liczbę "))
for dzielnik in range(2,a+1):
  if a%dzielnik == 0:
    print(dzielnik)
a = 4
b = 24
while b!=0:
  a,b = b, a%b
#min 
#max 
#suma
#dzielniki
