from Sapin import *
sapin= Sapin(5000)
boule1=Boule(15,"brown",5)
boule2=Boule(30,"red",10)
boule3=Boule(30,"yellow",7)
boule4=Boule(30,"red",10)
Guirlande1=GLumineuse(200,"blue",500,50)
Guirlande2=GLumineuse(200,"blue",500,50)
Guirlande3=GLumineuse(200,"blue",500,50)
Guirlande4=GLumineuse(200,"blue",500,50)
Guirlande5=GLumineuse(200,"blue",500,50)

sapin.affichage()
print("---")
sapin.ajouter(Guirlande2)
sapin.ajouter(Guirlande1)
sapin.ajouter(Guirlande3)
sapin.ajouter(Guirlande4)
sapin.affichage()
print("---")
#sapin.supprimer(boule1)
sapin.affichage()
sapin.DessinSapin()
sapin.DessinDeco()



turtle.exitonclick()
