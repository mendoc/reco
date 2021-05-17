# Reco
Reco est un utilitaire pour archiver des fichiers.

## Présentation
Ce dépôt a pour but de présenter le projet, le fonctionnement, les cas d'usage et permettre à qui le souhaite de contribuer à son évolution.

## Constat
Parfois nous avons des fichiers, documents, etc. dans nos appareils que nous ne consultons pas tout le temps mais que nous ne pouvons pas ou ne voulons pas effacer à cause de leur importance. Nous nous retrouvons ainsi avec des fichiers qui occuppent notre espace disque sans trop savoir quoi en faire.

Plusieurs solutions s'offrent à nous. Nous pouvons enregistrer nos fichiers dans des serveurs en ligne qui mettent à notre disposition un espace de stockage. Compte tenu de l'espace qui nous est alloué, nous sommes parfois obligés de faire le tri des documents à sauvegarder pour ne pas saturer rapidement la mémoire.

Une autre solution est de sauvegarder tous nos fichiers dans un disque dur externe.

**Reco** s'inscrit comme un solution supplémentaire. Il permettra de créer une version atomique de chaque fichier. En gros, il permet de faire passer un fichier de 1Go à un fichier de quelques centaines de Ko.

## Vocabulaire
Pour la compréhension des travaux certains termes et expressions sont à connaitre. Le necessaire se trouve dans le fichier [manifest](MANIFEST.md)

## Machine Learning
Pour réaliser cet utilitaire, on peut créer un modèle de machine learning.
- Type de problème : Classification
- Dataset :
  - Lien de téléchargement : [Lien](https://raw.githubusercontent.com/mendoc/reco/master/dataset.csv) (1.5 Mo)
  - Taille : 100 000 lignes et 5 colonnes
  - Colonnes : 
    - 4 features : *Nombre de bits (nb), Nombre de bits à 1 (nbu), Rang dans la sous famille (rang), Position du bit (pos)*
    - 1 target : *Valeur (1 ou 0)*

Le but est de trouver le meilleur modèle possible qui pourra être généralisé pour prédire la valeur d'un bit (0 ou 1) en fonction des features renseignés.
