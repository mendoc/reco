Ici sont recencées toutes les règles permettant de générer les bits

## Vocabulaire
    - element      : Suite de bits. Ex : 10001 ou 11101100
    - famille      : Ensemble d'éléments ayant le même nombre de bits. 
                     Les éléments 1001 et 1101 sont de la même famille
    - sous-famille : Ensemble d'éléments de la même famille ayant le même nombre de bits à 1. 
                     Ex : 1001 et 1100 sont de la même sous-famille

## Légende
    - nb   : nombre de bits total
    - nbu  : nombre de bits à 1
    - rang : rang d'un élément dans une sous-famille
    - pos  : position d'un bit dans un élément d'une sous-famille

## Règles
    - Lorsque nbu = 0 alors tous les bits de tous les éléments de la sous-famille sont à 0.
    - Lorsque nb = nbu alors tous les bits de tous les éléments de la sous-famille sont à 1.
    - Lorsque nbu = 0 ou nbu = nb alors la sous-famille ne contient qu'un seul élément.
    - Lorsque nbu = 1 ou nbu = nb-1 alors la sous-famille contient nb élément(s)
    - Le dernier bit du dernier élément d'une sous-famille est toujours égale à 0 sauf si nbu = nb.
    - Le nombre de sous-familles dans une famille est égale à nb+1.
