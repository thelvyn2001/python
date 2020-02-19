# -*- coding: utf8 -*-

#Listes
character = ["name1", "name2", "name3", "name4"]
print(character.index("name3")) #retrouve l'index d'une liste
character.append("name5") #inserer a la fin
character.insert(3, "bazlou") #insertion a une certaine place
character[1] = "newName" #remplacement d'une donées
print(character)
character.pop() #suppression dernier élément de la liste ou .pop(4) pour le 5ee indice0
character.remove("name3")

character1 = ["name1", "name2", "name3", "name4"]
x = len(character1)
print("nb element in the list : " + str(x))
for i in character1:
    print(i)

for i in range(x):
    print(character[i])

list2 = ["henry",25, "steph"]
print(list2)
print("list2 indice 1 : " + str(list2[1]))

#Dictionnaires
dico = {'three': 'trois', 'one': 'un', 'two': 'deux'} #association clef:valeur
print(dico)
dico.update({"one": "UN", "two": "DEUX"})  #mise a jour
dico["three"] = "Trois"
print(dico) 
dico.pop("one") #supression  ou del dico["one"]
print(dico)
print(dico["three"])  #acces à une valeur avec la cle
print(dico.get("three")) #idem
dico["ten"] = "dix"
for z in dico:  #loop to display index
    print("index : " + z)
for z in dico:  #loop to display value
    print("value : " + dico[z])
for x, y in dico.items(): #loop to display index and value
    print("index : " + x + " - value = " + y)

print("taille du dictionnaire : " + str(len(dico)))

phrase = "je suis un pro du développement informatique"
lenPhrase = len(phrase)
stars = ""
for i in range(lenPhrase):
    stars += "*"
print(stars)
print(phrase)
print(stars)




#copy dictionnary
newDico = dico.copy()
print(newDico)

#tuples  données qui ne bougent pas --> immuables
paris = (48.856578, 2.351828)
print("coordonnées GPS Paris : " + str(paris))
print(paris)