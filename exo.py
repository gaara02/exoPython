import random
#Exo1
print("Bienvenue sur la page de determination d'année bissextile")

annee = int(input("Veuillez saisir une annee : "))

if annee % 4 == 0 and annee % 100 !=0 or annee % 400 ==0  : {
    print("Cette annee est une annee bissextile")
} 
else : {
    print("Cette année n'est pas une année bissextile")

}
    
#Exo2

D1 =  random.randrange(1,7)   
D2 = random.randrange(1,7)

somme = D1 + D2
print("la somme du lancé de Dé est egal a ",somme)

def lance(n) :
    for i in range(n) : 
       resultat = i = random.randrange(1,7)
       print(resultat)
        
lance(2)

#Exo3

entier = int(input("Saisir un entier : "))
i = 0
for i in range (entier+1) : 
    resultat = i**2
    print(resultat)

#Exo4

nb1 = int(input("Saisir un nombre : "))  
nb2 = int(input("Saisir un autre nombre : "))  
somme = 1
for i in range(nb1,nb2+1) : 
    
    somme*=i
print(somme)

# Exo5  
table = [2,4,5,6,7,9,12,16,17,20]
nombre = 0
nombre2= 0
for i in (table):
    if i%2 == 0 :
        nombre +=1
             
        
    else : 
        nombre2 +=1
        

print("le nombre de nombre pair est ", nombre) 
print("le nombre de nombre impair est ", nombre2)

#Exo6

def decaleCircDroite(table) :
    
    table_valeur = table[-1]
    nouvelle_table = [table_valeur] + table[:-1]
    return nouvelle_table
print("tableau avant décalage")
table = [12, 21, 10, 11, 0, 1, 6, 8]
print(table)
print("tableau apres décalage")

print(decaleCircDroite(table))

#exo7
def bin2dec(nBin):
    convert = int(nBin,2)
    return convert
nBin = '10000001'
nDec = bin2dec(nBin)
print('Le nombre binaire  (code entier naturel) '+ str(nBin)+' se convertit en base 10 : '+ str(nDec))

def dec2bin(nDec) : 
    nBin  = bin(nDec)[2:]
    return nBin
nDec = 5
nBin = dec2bin(nDec)

print("le binaire de " + str(nDec) + "en base 2 est" + " "+ str(nBin))

#Exo8

n = int(input("Veuillez saisir un nombre : "))
somme = 0
for i in range(n+1) : 
    somme +=i
print("la somme total est ", somme)    

#Exo9
def puissance(n,p):
    if(p==0):
        return 1
    else:
        return n*puissance(n,p-1)


n = -1
while n<=0 or p<=0:
    n= int(input("saisir le nombre:"))
    p= int(input("saisir la puissance:"))
print("{} puissance {} est : {}".format(n,p,puissance(n,p)))

#Exo10

def fibonacci(n):
    if n <= 0:
        return "La valeur de 'n' doit être un entier positif."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Entrez un entier positif pour calculer le nième terme de la suite de Fibonacci : "))

result = fibonacci(n)


print("Le nième terme de la suite de Fibonacci est :", result)

#exo11
tab = random.sample(range(1,100), 10)
print(*tab,sep=",")

#Exo12

def echanger(tab, i, j):
    #Échange les valeurs aux indices i et j dans le tableau tab.
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

# Création du tableau avec des chiffres aléatoires entre 1 et 100
tableau = [random.randint(1, 100) for _ in range(10)]

# Tri du tableau avec l'algorithme de tri par sélection
n = len(tableau)
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if tableau[j] < tableau[min_idx]:
            min_idx = j
    echanger(tableau, i, min_idx)

# Affichage des valeurs séparées par une virgule
resultat = ', '.join(str(nombre) for nombre in tableau)
print(resultat)

#Exo13

def factoriel(n):
    if(n==0):
        return 1
    else:
        return n*factoriel(n-1)

n = -1
while n<=0:
    n= int(input("Donner le nombre:"))
print("Le fatoriel de {} est : {}".format(n,factoriel(n)))

#Exo14

def generer_phrase(tableau_mots):
    
    random.shuffle(tableau_mots)  
    phrase = ' '.join(tableau_mots)  
    phrase = phrase.capitalize() + '.'  
    print(phrase)


mots = ['chien', 'chat', 'oiseau', 'maison', 'arbre', 'soleil']
generer_phrase(mots)




