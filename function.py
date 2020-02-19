import math

def afficher_paroles():
    print("qui s'enfuit deja")
    print("oublier le temps")

afficher_paroles()

def repeter_paroles():
    afficher_paroles()
    afficher_paroles()

repeter_paroles()

def afficher_deux_fois(pierre):
    print(pierre)
    print(pierre)

afficher_deux_fois('bonjour')
afficher_deux_fois(45)
afficher_deux_fois('jean' * 3)

jean = "jacques"
afficher_deux_fois(jean)
