# -*- coding: utf-8 -*-
"""
Created on Nov 30 2023

@author: Mazard Pierre

#Calculatrice
"""

#Importation de fonctions externes (librairies) :
    
    
#Définition locale de fonctions : 
def nombre_valide(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(""""
                  ! Erreur ! Veuillez entrer un nombre valide !
                  """)
def operateur_valide(prompt):
    while True:
        cal = input(prompt)
        if cal in {"+", "-", "*", "/"}:
            return cal
        else:
            print("""
                  ! Erreur ! ==> veuillez spécifier un opérateur valide !
                   """)
#Déclaration des variables : 

historique = []    

#Corps principal du programme : 

continuer = True

while continuer: 
    
    print("""
          Voici une calculatrice basique permettant d'effectuer une opération entre deux nombres.
           """ ) 
    a = nombre_valide("""Saisir la valeur du premier nombre :
    => : """)
    
    operateur = operateur_valide("""
    Saisir l'opérateur souhaité :
    Addition          => +
    Soustraction      => -
    Multiplication    => *
    Division          => /            
                
    ==> : """)
    
    b = nombre_valide("""
Saisir la valeur du second nombre : 
    => : """)           
    
    if operateur == "+":
        result = a + b
        print (f"""
                       ==> La somme de {a} et de {b} est égale à {result}
               
               """)
    if operateur == "-":
        result = a - b
        print (f"""
                       ==> La soustraction de {a} par {b} est égale à {result}
               
               """)            
    if operateur == "*":
        result = a * b
        print (f"""
                       ==> Le produit de {a} et de {b} est égal à {result}
               
               """)
    if operateur == "/":
        result = a / b
        print (f"""
                       ==> Le rapport de {a} par {b} est égal à {result}
               
               """)
               
    historique.append(f"{a} {operateur} {b} = {result}")           
    choix = input("""
                  Souhaitez-vous continuer, voir l'historique ou effacer l'historique ?

Continuer / Historique / Effacer / Non ?

=> """)
    
    if choix == "Non":
        print("""                        Au revoir !
              """)
        continuer = False
    elif choix == "Historique":
        print("\n".join(historique))
    elif choix == "Effacer":
        historique.clear()