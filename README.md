# Reco
Reco est un utilitaire pour archiver des fichiers.

## Présentation
Ce projet a pour but de présenter le projet, le fonctionnement, les cas d'usage et permettre à qui le souhaite de contribuer à son évolution.

## Constat
Parfois nous avons des fichiers, documents, etc. dans nos appareils que nous ne consultons pas tout le temps mais que nous ne pouvons pas ou le voulons pas effacer à cause de leur importance. Nous nous retrouvons ainsi avec des fichiers qui occuppent notre espace disque sans trop savoir quoi en faire. 

Plusieurs solutions s'offrent à nous. Nous pouvons enregistrer nos fichiers dans des serveurs en ligne qui mettent à notre disposition un espace de stockage. Compte tenu de l'espace qui nous alloué, nous sommes parfois obligés de faire le tri des documents à savergarder pour ne pas saturer rapidement la mémoire.

Une autre solution est de sauvegarder tous nos fichiers dans un disque dur externe.

**Reco** s'inscrit comme un solution supplémentaire. Il permettra de créer version atomique de charque fichier. En gros, il permettra de passer fichier de 1Go à un fichier quelques centaines de Ko.

## Travail à faire
Pour réaliser cet utilitaire, il sera question de créer un modèle de machine learning.
- Type de problème : Classification
- Dataset :
  - Lien de téléchargement : [Lien](https://raw.githubusercontent.com/mendoc/reco/master/dataset.csv)
  - Taille : 100 000 lignes et 5 colonnes
  - Colonnes : 
    - 4 features : *Nombre de bits, Nombre de bits à 1, Rang dans la sous famille, Position du bit*
    - 1 target : *Valeur*

Le but est de trouver le meilleur modèle possible qui pourra être généralisé pour prédire les features d'un autre dataset similaire.
