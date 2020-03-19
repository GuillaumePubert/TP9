class Sapin:
    def __init__(self,masseMax,masseTotale=0):
        self._masseMax=masseMax
        self._masseTotale=masseTotale
    def getMasseMax(self):
        return  self._masseMax
    def getMasseTotale(self):
        if self._masseTotale!=0:
            return (str(self._masseTotale))
        else:
            return("0")
    def ajouter(self,deco,Listedeco,Listemasse):
        Listedeco.append(deco)
        Listemasse.append(Decoration.getMasseDeco(deco))
    def supprimer(self,deco,Listedeco,Listemasse):
        Listedeco.remove(deco)
        Listemasse.remove(Decoration.getMasseDeco(deco))
    def affichage(self,Listedeco,Listemasse):
        counter=0
        for k in  Listemasse:
            counter=counter+k
        if counter!=0:
            print("Il peut supporter ",self.getMasseMax(),"g et contient ",counter,"g de décorations.")
        else:
            print("Il peut supporter ",self.getMasseMax(),"g et contient aucune décoration")
        for i in Listedeco:
            i.affichage()
class Decoration:
    def __init__(self,massedeco,couleurdeco):
        self._massedeco=massedeco
        self._couleurdeco=couleurdeco
    def getMasseDeco(self):
        return self._massedeco
    def getCouleurDeco(self):
        return self._couleurdeco

class Boule(Decoration):
    def __init__(self,massedeco,couleurdeco,diametre):
        Decoration.__init__(self,massedeco,couleurdeco)
        self._diametre=diametre
    def getDiametre(self):
        return self._diametre
    def affichage(self):
        print("Boule ",Boule.getCouleurDeco(self),"de ",Boule.getDiametre(self)," cm de diamètre, possedant pesant ",Boule.getMasseDeco(self),"g")



class Guirlande(Decoration):
    def __init__(self,massedeco,couleurdeco,longueur):
        Decoration.__init__(self,massedeco,couleurdeco)
        self._longueur=longueur
    def getLongueur(self):
        return self._longueur

class GLumineuse(Guirlande):
    def __init__(self,massedeco,couleurdeco,longueur,nblumieres):
        Guirlande.__init__(self,massedeco,couleurdeco,longueur)
        self._nblumieres=nblumieres
    def getNbLumieres(self):
        return self._nblumieres
    def affichage(self):
        print("Guirlande lumineuse ",GLumineuse.getCouleurDeco(self),"de ",GLumineuse.getLongueur(self)," cm de long, possedant", GLumineuse.getNbLumieres(self), "lumières et pesant ",GLumineuse.getMasseDeco(self),"g")

