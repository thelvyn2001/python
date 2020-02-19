class Utilisateur:
    #attributs
    statut = "inscrit"
    age = 0

    #methodes
    def setNom(self, n):
        self.nom = n

#intanciation  de la classe - nouvelle instance de classe
pierre = Utilisateur()
mathilde = Utilisateur()
#pierre et mathlide sont des objets
print(pierre)
print(mathilde)

pierre.setNom("Pierre")
print(pierre.nom + " est " + pierre.statut + "et il a " + str(pierre.age) + " ans")
pierre.age = 10
print(pierre.nom + " est " + pierre.statut + "et il a maintennat " + str(pierre.age) + " ans")

#Encapsulation
class Utilisateur1:
    anciennete = 0 #variable de classe 

    #constructor
    def __init__(self, nom1, age1):
        self.user_name = nom1  # = this.user_name=name en JS
        self.user_age = age1

    #methode
    def getNom(self):
        print("Salut, je suis ", self.user_name + " et j ai ", self.user_age)

steph = Utilisateur1("steph", 51)
steph.getNom()


#héritage de classe
class Client(Utilisateur1):
    is_client = True

jean = Client("jean", 25)
jean.getNom()

#surcharge
class Fournisseur(Utilisateur1):
    is_fournisseur = True
    tva = 10

    def __init__(self, nom1, age1, mail):
        Utilisateur1.__init__(self, nom1, age1) #etend la class init
        self.user_mail = mail

    def getNameFrs(self):
        print("le fournisseur est ", self.user_name + " et il a ", str(self.user_age) + " ans et son taux de TVA est de : ", str(self.tva) + "% et son mail est ", self.user_mail ) 


calberson = Fournisseur("calbseron", 52, "henrysteph60@gmail.com")
calberson.tva = 20
calberson.getNameFrs()

#test type d'instance
print(isinstance(calberson, Utilisateur1)) #true
print(isinstance(calberson, Fournisseur))  #true
print(isinstance(calberson, Utilisateur))   #false 

#test d'héritage d'une class
print(issubclass(Utilisateur, Utilisateur1)) #false
print(issubclass(Fournisseur, Utilisateur1)) #true



class Tabnoir:
    #constructor
    def __init__(self):
        self.surface = ""
    #methodes    
    def ecrireMessage(self, mess_ecrire):
        if self.surface !="":
            self.surface+= "\n"
        self.surface +=mess_ecrire
        
    def lireMessage(self):
        print(self.surface)
    
    def effacerMessage(self):
        self.surface=""

msg1 = Tabnoir()
msg1.ecrireMessage("ecrire un message")
msg1.lireMessage()
msg1.ecrireMessage("ecrire un deuxieme message")
msg1.lireMessage()



