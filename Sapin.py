import turtle
import random
import math

class Sapin:
    def __init__(self,masseMax,listedeco=[],masseTotale=0):
        self._masseMax=masseMax
        self._masseTotale=masseTotale
        self._listedeco=listedeco
    def getMasseMax(self):
        return  self._masseMax
    def getMasseTotale(self):
        if self._masseTotale!=0:
            return (str(self._masseTotale))
        else:
            return("0")

    def ajouter(self,deco):
        self._listedeco.append(deco)
        print("")
        self._masseTotale+=Decoration.getMasseDeco(deco)
    def supprimer(self,deco):
        self._listedeco.remove(deco)
        self._masseTotale-=Decoration.getMasseDeco(deco)
    def affichage(self):
        if self._masseTotale!=0:
            print("Il peut supporter ",self.getMasseMax(),"g et contient ",self._masseTotale,"g de décorations.")
            if self._masseTotale>self._masseMax:
                print("Attention... le sapin risque de s'éffondrer")
        else:
            print("Il peut supporter ",self.getMasseMax(),"g et contient aucune décoration.")
        for i in self._listedeco:
            i.affichage()
    def DessinSapin(self):
        turtle.hideturtle()
        turtle.speed('fastest')
        turtle.color('brown')
        turtle.begin_fill()
        turtle.fd(30)
        turtle.right(90)
        turtle.fd(60)
        turtle.right(90)
        turtle.fd(60)
        turtle.right(90)
        turtle.fd(60)
        turtle.right(90)
        turtle.fd(30)
        turtle.end_fill()
        turtle.color('green')
        turtle.begin_fill()
        turtle.fd(200)
        turtle.goto(0,200)
        turtle.goto(-200,0)
        turtle.goto(0,0)
        turtle.end_fill()
    def ChoixDeco(self,x,y,i):
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.color(Decoration.getCouleurDeco(i))
        if i.name()=="boule":
            turtle.begin_fill()
            turtle.circle(Boule.getDiametre(i))
            turtle.end_fill()
        else:
            if y<=100:
                a=math.copysign(1,x)
                if x >0:
                    turtle.setheading(180)
                else:
                    turtle.setheading(0)
                angle=random.randint(0,45)
                turtle.left(-a*angle)
                turtle.pensize(6)
                turtle.fd((Guirlande.getLongueur(i))/10)
            else:
                turtle.setheading(-45)
                angle=random.randint(0,90)
                turtle.right(angle)
                turtle.pensize(6)
                turtle.fd((Guirlande.getLongueur(i))/10)

    def DessinDeco(self):
        for i in self._listedeco:
            x=random.randint(-180,180)
            y=300
            if x>=0:
                while y>=200 or y>-x+180:
                    y=random.randint(20,180)
                Sapin.ChoixDeco(self,x,y,i)
            elif x<=0:

                while y>=200 or y<0 or y>x+180:
                    y=random.randint(20,180)
                Sapin.ChoixDeco(self,x,y,i)
class Decoration:
    def __init__(self,massedeco,couleurdeco):
        self._massedeco=massedeco
        self._couleurdeco=couleurdeco
    def getMasseDeco(self):
        return self._massedeco
    def getCouleurDeco(self):
        return self._couleurdeco
    def affichage(self):
        pass

class Boule(Decoration):
    def __init__(self,massedeco,couleurdeco,diametre):
        Decoration.__init__(self,massedeco,couleurdeco)
        self._diametre=diametre
    def getDiametre(self):
        return self._diametre
    def affichage(self):
        print("Boule ",Boule.getCouleurDeco(self),"de ",Boule.getDiametre(self)," cm de diamètre, possedant pesant ",Boule.getMasseDeco(self),"g")
    def name(self):
        return ("boule")


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
    def name(self):
        return ("guirlande")




