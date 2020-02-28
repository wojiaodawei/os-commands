#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from stat import *


def mycopy(frome,to):
        a=os.listdir(frome) ## liste des elements du dossier frome
        inoeuds={}
        for i in range(len(a)):
                inode=os.stat(frome+'/'+a[i])[ST_INO] #on recupère les numeros d'inoeud
                if inode not in inoeuds: 
                        inoeuds[inode]=to+'/'+a[i] #ajoute l'inoeud dans un dictionnaire avec son chemin
                        if os.path.isfile(frome+'/'+a[i]): #si c'est un fichier
                                fic=open(frome+'/'+a[i],"r") #on l'ouvre
                                lire=fic.read() #puis on le lit
                                fic1=open(to+'/'+a[i],"w") #on créé le nouveau fichier
                                fic1.write(lire) #dans lequel on écrit le fichier à copier
                                fic.close() #on ferme le descripteur
                                fic1.close()
                        else: #si c'est un répertoire
                                try:
                                        os.mkdir(to+'/'+a[i]) #si l'élément est un dossier on en crée un nouveau sauf si il existe deja
                                except:
                                        pass
                                mycopy(frome+'/'+a[i],to+'/'+a[i]) # appel recursif de notre fonction pour copier dans le dossier
                else:
                        os.link(inoeuds[inode],to+'/'+a[i]) #si même inoeud on crée un hardlink vers le fichier qui a le même inoeud
                

if len(sys.argv)!=3: #si il n'y a pas 2 arguments from et to d'entrés
        print("Erreur vous devez entrer 2 arguments !")
elif (os.path.isdir(sys.argv[1]) and os.path.isdir(sys.argv[2]))==False: # si au moins 1 des 2 arguments n'est pas un dossier
        print("Erreur les arguments doivent être des dossiers")
elif sys.argv[1]!=sys.argv[2]: #si les dossiers sont bien distincts
        mycopy(sys.argv[1],sys.argv[2])
else: #sinon
        print("Erreur, le dossier d'arrivée est le même que celui de départ !")

