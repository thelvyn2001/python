#importation avec création d'un alias
import functionOne as b

#ou si pas d'alias  functionOne.disBonjour
b.disBonjour("steph")

#ou si pas d'alias  y = functionOne.somme(10,20)
y = b.somme(20,30)
print("somme de 20 + 30 = " + str(y))

#ou si pas d'alias print(dir(functionOne))
print(dir(b)) #liste des éléments du module

nb1 = input("nb 1 : ")
nb2 = input("nb 2 : ")
tot = int(nb1) + int(nb2)
tot1 = nb1 + nb2
print(type(tot))
print(type(tot1))
print(str(nb1) + " + " + str(nb2) + " = " + str(tot))